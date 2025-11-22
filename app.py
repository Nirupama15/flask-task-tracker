from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import sqlite3
import os
from datetime import datetime, date
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# Initialize extensions
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

# Database path
DB_PATH = os.path.join('/tmp', 'tasks.db') if os.environ.get('RENDER') else 'tasks.db'

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, username, email FROM users WHERE id = ?', (user_id,))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        return User(user_data[0], user_data[1], user_data[2])
    return None

# Database initialization
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Tasks table with user_id
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL,
                  task TEXT NOT NULL,
                  completed INTEGER DEFAULT 0,
                  priority TEXT DEFAULT 'medium',
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    conn.commit()
    conn.close()

# Initialize database
with app.app_context():
    init_db()

# Get tasks for current user
def get_user_tasks(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
    tasks = c.fetchall()
    conn.close()
    return tasks

# Get today's tasks
def get_today_tasks(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = date.today().strftime('%Y-%m-%d')
    c.execute('''SELECT * FROM tasks WHERE user_id = ? 
                 AND DATE(created_at) = ? ORDER BY created_at DESC''', (user_id, today))
    tasks = c.fetchall()
    conn.close()
    return tasks

# Routes
@app.route('/')
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters!', 'error')
            return redirect(url_for('register'))
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                     (username, email, hashed_password))
            conn.commit()
            conn.close()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        
        except sqlite3.IntegrityError:
            flash('Username or email already exists!', 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please enter both username and password!', 'error')
            return redirect(url_for('login'))
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT id, username, email, password FROM users WHERE username = ?', (username,))
        user_data = c.fetchone()
        conn.close()
        
        if user_data and bcrypt.check_password_hash(user_data[3], password):
            user = User(user_data[0], user_data[1], user_data[2])
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    all_tasks = get_user_tasks(current_user.id)
    today_tasks = get_today_tasks(current_user.id)
    
    # Calculate stats
    total_tasks = len(all_tasks)
    completed_tasks = len([t for t in all_tasks if t[3] == 1])
    pending_tasks = total_tasks - completed_tasks
    today_total = len(today_tasks)
    today_completed = len([t for t in today_tasks if t[3] == 1])
    
    return render_template('dashboard.html', 
                         tasks=all_tasks,
                         today_tasks=today_tasks,
                         total=total_tasks,
                         completed=completed_tasks,
                         pending=pending_tasks,
                         today_total=today_total,
                         today_completed=today_completed,
                         user=current_user)

@app.route('/add', methods=['POST'])
@login_required
def add_task():
    task = request.form.get('task')
    priority = request.form.get('priority', 'medium')
    
    if task:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('INSERT INTO tasks (user_id, task, priority) VALUES (?, ?, ?)',
                 (current_user.id, task, priority))
        conn.commit()
        conn.close()
        flash('Task added successfully!', 'success')
    
    return redirect(url_for('dashboard'))

@app.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = 1 WHERE id = ? AND user_id = ?', 
             (task_id, current_user.id))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/uncomplete/<int:task_id>')
@login_required
def uncomplete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = 0 WHERE id = ? AND user_id = ?', 
             (task_id, current_user.id))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', 
             (task_id, current_user.id))
    conn.commit()
    conn.close()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:task_id>', methods=['POST'])
@login_required
def edit_task(task_id):
    new_task = request.form.get('task')
    priority = request.form.get('priority', 'medium')
    
    if new_task:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('UPDATE tasks SET task = ?, priority = ? WHERE id = ? AND user_id = ?',
                 (new_task, priority, task_id, current_user.id))
        conn.commit()
        conn.close()
        flash('Task updated successfully!', 'success')
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully!', 'success')
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')