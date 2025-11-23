# 📝 Daily Task Tracker

A simple and elegant Flask-based web application for managing daily tasks with user authentication, calendar integration, and priority management.

---

## 🌐 Live Demo & Repository

**Hosted App URL:** [https://flask-task-tracker-fn5m.onrender.com](https://flask-task-tracker-fn5m.onrender.com)

**GitHub Repository:** [https://github.com/Nirupama15/flask-task-tracker](https://github.com/Nirupama15/flask-task-tracker)


### Core Functionality (Required)
The application meets all the required functionality from the assignment:

- ✅ **Add Tasks** - Create new daily tasks with descriptions
- ✅ **Edit Tasks** - Modify existing task details
- ✅ **Delete Tasks** - Remove tasks from the list
- ✅ **Mark as Completed** - Toggle task completion status
- ✅ **View Tasks** - Display all tasks in a simple, organized list

### Bonus Features (Implemented)
The following bonus features have been successfully implemented:

- 💾 **SQLite Database Integration** - All tasks are stored persistently in a database
- 🔄 **Dynamic Page Rendering** - Tasks are dynamically displayed using Jinja2 templates
- 🔐 **User Authentication System** - Secure registration and login functionality
- 👤 **Multi-User Support** - Each user has their own private task list
- 📅 **Calendar Integration** - Tasks can be scheduled for specific dates
- 🎯 **Priority Management** - Three priority levels (High, Medium, Low)
- 📊 **Dashboard Statistics** - Real-time metrics showing task progress
- 🌅 **Today's Tasks Section** - Special section highlighting current day tasks
- 🔍 **Date Filtering** - View tasks by specific date
- ⚡ **Smart Validations** - Prevents invalid operations (past dates, future completions)
- 🎨 **Modern UI/UX** - Professional design with smooth animations
- 📱 **Fully Responsive** - Works seamlessly on all devices
- 🗑️ **Delete Confirmation** - Modal popup for safe task deletion

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask (Python 3.x) |
| **Template Engine** | Jinja2 (default with Flask) |
| **Database** | SQLite |
| **Authentication** | Flask-Login, Flask-Bcrypt |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Icons** | FontAwesome 6.4.0 |
| **Hosting Platform** | Render |
| **Version Control** | Git & GitHub |

---

## 🚀 How to Run Locally

Follow these steps to run the project on your local machine:

### Prerequisites
Before starting, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Instructions

#### Step 1: Clone the Repository
```bash
git clone https://github.com/Nirupama15/flask-task-tracker.git
cd flask-task-tracker
```

#### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

#### Step 3: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

#### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install all required packages:
- Flask==3.0.0
- Flask-Login==0.6.3
- flask-bcrypt==1.0.1
- gunicorn==21.2.0

#### Step 5: Run the Application
```bash
python app.py
```

You should see output like:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

#### Step 6: Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

#### Step 7: Stop the Server
Press `Ctrl+C` in the terminal to stop the Flask development server.

---

## 🌐 Hosting Platform

**Platform Used:** Render ([render.com](https://render.com))

### Why Render?
- ✅ Free tier available
- ✅ Easy GitHub integration
- ✅ Automatic deployments on git push
- ✅ Built-in SSL certificates
- ✅ Simple configuration

### Deployment Configuration
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Instance Type:** Free tier

### Deployment Process
1. Created GitHub repository with project code
2. Connected repository to Render
3. Configured build and start commands
4. Deployed application (auto-deploys on git push)

---

## 📦 Project Structure
```
flask-task-tracker/
│
├── app.py                    # Main Flask application with all routes
├── requirements.txt          # Python package dependencies
├── render.yaml              # Render deployment configuration
├── README.md                # Project documentation (this file)
├── .gitignore               # Git ignore patterns
│
├── templates/               # HTML templates folder
│   ├── landing.html         # Home/landing page
│   ├── login.html           # User login page
│   ├── register.html        # User registration page
│   └── dashboard.html       # Main task dashboard
│
└── tasks.db                 # SQLite database (auto-generated)
```

---

## 💡 Extra Features Added

Beyond the basic requirements, I implemented several creative features:

### 1. User Authentication System
- **Registration:** New users can create accounts with username, email, and password
- **Login:** Secure authentication with password hashing
- **Sessions:** Persistent user sessions across page reloads
- **Password Security:** bcrypt hashing for password protection

### 2. Calendar-Based Task Scheduling
- **Date Picker:** Visual calendar for selecting task due dates
- **Today's Tasks:** Special section highlighting tasks due today
- **Date Filtering:** View all tasks scheduled for a specific date
- **Future Task Management:** Smart handling of future-dated tasks

### 3. Priority Management System
- **Three Levels:** High (red), Medium (gold), Low (blue)
- **Visual Indicators:** Color-coded badges and backgrounds
- **Priority Selection:** Choose priority when creating/editing tasks

### 4. Smart Validations
- **No Past Dates:** Cannot create tasks for dates that have passed
- **Future Task Protection:** Cannot mark future tasks as complete
- **Date-Aware Completion:** Only today's or past tasks can be completed
- **Form Validation:** Client-side and server-side validation

### 5. Enhanced User Experience
- **Statistics Dashboard:** Real-time metrics (Total, Completed, Pending, Today)
- **Flash Messages:** User-friendly feedback for all actions
- **Confirmation Modals:** Popup confirmation before deleting tasks
- **Inline Editing:** Edit tasks without page reload
- **Responsive Design:** Perfect on desktop, tablet, and mobile

### 6. Beautiful UI Design
- **Premium Color Scheme:** Ivory, black, and gold palette
- **Smooth Animations:** Subtle hover effects and transitions
- **Modern Icons:** FontAwesome icons throughout
- **Clean Layout:** Intuitive and uncluttered interface

---

## 🤔 Difficulties Faced

### Challenge 1: Database Persistence on Render
**Problem:** 
- Render's free tier uses ephemeral storage
- SQLite database couldn't write to the default location
- Database would reset on service restart

**Solution:**
- Used `/tmp` directory for database storage on Render
- Modified database path logic to detect Render environment
- Added environment variable check: `os.environ.get('RENDER')`

**Code Implementation:**
```python
DB_PATH = os.path.join('/tmp', 'tasks.db') if os.environ.get('RENDER') else 'tasks.db'
```

**Learning:** Understanding the difference between ephemeral and persistent storage in cloud environments.

---

### Challenge 2: Implementing Date Validations
**Problem:**
- Users should not complete tasks scheduled for future dates
- Need to prevent adding tasks for past dates
- Date comparison between user input and current date

**Solution:**
- Implemented server-side date validation using Python's datetime module
- Added client-side validation with HTML5 date input attributes
- Created custom route logic to check task dates before completion

**Code Implementation:**
```python
# Validate date is not in the past
due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
if due_date_obj < date.today():
    flash('Cannot add tasks for past dates!', 'error')
    return redirect(url_for('dashboard'))
```

**Learning:** Importance of both client-side and server-side validation for data integrity.

---

### Challenge 3: Responsive Design Across Devices
**Problem:**
- Layout breaking on mobile devices
- Task cards not fitting properly on small screens
- Navigation menu overflow issues

**Solution:**
- Implemented comprehensive CSS media queries
- Used CSS Flexbox and Grid for flexible layouts
- Added mobile-first design approach
- Tested on multiple screen sizes

**Code Implementation:**
```css
@media (max-width: 768px) {
    .task-item {
        flex-direction: column;
        align-items: flex-start;
    }
    .task-actions {
        width: 100%;
        flex-direction: column;
    }
}
```

**Learning:** Mobile-first design principles and the importance of testing on real devices.

---

### Challenge 4: User Authentication and Session Management
**Problem:**
- Securely storing passwords
- Managing user sessions across routes
- Protecting routes from unauthorized access

**Solution:**
- Used Flask-Login extension for session management
- Implemented bcrypt for password hashing
- Added @login_required decorators to protected routes
- Created User class for Flask-Login compatibility

**Code Implementation:**
```python
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
@login_required
def dashboard():
    # Protected route logic
```

**Learning:** Best practices for web application security and authentication patterns.

---

### Challenge 5: Database Schema Changes During Development
**Problem:**
- Initially built app without due_date column
- Adding new column required database migration
- Existing data would be lost

**Solution:**
- Documented the need to delete old database
- Created clear instructions for local testing
- Ensured proper schema on deployment

**Code Implementation:**
```python
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL,
              task TEXT NOT NULL,
              completed INTEGER DEFAULT 0,
              priority TEXT DEFAULT 'medium',
              due_date DATE NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES users (id))''')
```

**Learning:** Importance of planning database schema upfront and using migration tools for production.

---

### Challenge 6: Cold Start Delay on Free Hosting
**Problem:**
- Render's free tier puts service to sleep after 15 minutes
- First request takes 30-60 seconds to wake up
- Poor user experience for first-time visitors

**Solution:**
- Documented the limitation in README
- Suggested using UptimeRobot to keep service awake
- Provided alternative hosting options

**Learning:** Understanding trade-offs of free hosting tiers and optimization strategies.

---

## 🎓 Key Learnings

1. **Flask Framework Mastery**
   - Routing and URL handling
   - Template rendering with Jinja2
   - Form handling and validation
   - Session management

2. **Database Operations**
   - SQLite CRUD operations
   - Database schema design
   - SQL injection prevention
   - Foreign key relationships

3. **Web Security**
   - Password hashing with bcrypt
   - Session-based authentication
   - Protected routes
   - Input validation

4. **Frontend Development**
   - Responsive CSS design
   - JavaScript for interactivity
   - CSS animations and transitions
   - Mobile-first approach

5. **Deployment & DevOps**
   - Git version control
   - Cloud platform deployment
   - Environment configuration
   - Continuous deployment

---

## 🔒 Security Features

- **Password Hashing:** All passwords encrypted using bcrypt
- **Session Management:** Secure session handling with Flask-Login
- **SQL Injection Prevention:** Parameterized queries throughout
- **User Data Isolation:** Each user can only access their own tasks
- **Protected Routes:** Login required for all task operations
- **CSRF Protection:** Built-in Flask security features

---

## 📱 Responsive Design

The application is fully responsive and tested on:

- **Desktop:** 1920x1080, 1366x768
- **Tablet:** iPad (768x1024), iPad Pro (1024x1366)
- **Mobile:** iPhone (375x667), Samsung Galaxy (360x640)

**Breakpoints:**
- Large screens: 1200px+
- Medium screens: 768px - 1199px
- Small screens: 480px - 767px
- Extra small: < 480px

---

## 🎨 Design System

### Color Palette
- **Primary Background:** Ivory (#f5f5dc, #fffef7)
- **Dark Background:** Charcoal (#2c2c2c, #1a1a1a)
- **Accent:** Gold (#d4af37)
- **Success:** Green (#4caf50)
- **Warning:** Orange (#ff9800)
- **Error:** Red (#f44336)
- **Info:** Blue (#2196f3)

### Typography
- **Font Family:** Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- **Headings:** Bold, larger sizes
- **Body:** Regular weight, readable sizes

### Icons
- **Library:** FontAwesome 6.4.0
- **Usage:** Consistent iconography throughout the app

---

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tasks Table
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0,
    priority TEXT DEFAULT 'medium',
    due_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

---

## 🐛 Known Limitations

### 1. Database Persistence (Render Free Tier)
- **Issue:** Database stored in `/tmp` directory resets when service sleeps
- **Impact:** All tasks will be lost after 15 minutes of inactivity
- **Workaround:** Use UptimeRobot to keep service active, or upgrade to paid tier
- **Long-term Solution:** Use external PostgreSQL database

### 2. Cold Start Delay
- **Issue:** First request after inactivity takes 30-60 seconds
- **Impact:** Poor initial user experience
- **Workaround:** Use UptimeRobot to ping service every 5-10 minutes
- **Long-term Solution:** Upgrade to paid hosting plan

### 3. No Email Verification
- **Issue:** Users can register with any email without verification
- **Impact:** Potential for fake accounts
- **Future Enhancement:** Add email verification system

---

## 🔮 Future Enhancements

Potential features for future versions:

1. **Task Categories/Tags**
   - Organize tasks by category (Work, Personal, Shopping, etc.)
   - Filter tasks by tags

2. **Task Sharing**
   - Share tasks with other users
   - Collaborative task lists

3. **Recurring Tasks**
   - Daily, weekly, monthly recurring tasks
   - Automatic task creation

4. **Email Notifications**
   - Reminder emails for upcoming tasks
   - Daily task summary emails

5. **Task Export**
   - Export tasks to CSV or PDF
   - Print-friendly view

6. **Dark Mode**
   - Toggle between light and dark themes
   - User preference storage

7. **Task Attachments**
   - Attach files or images to tasks
   - Cloud storage integration

8. **Search & Filter**
   - Search tasks by keyword
   - Advanced filtering options

9. **PostgreSQL Migration**
   - Move from SQLite to PostgreSQL
   - Better for production use

10. **Mobile App**
    - Native iOS and Android apps
    - Push notifications

---

## 📝 API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/` | GET | Landing page | Public |
| `/register` | GET, POST | User registration | Public |
| `/login` | GET, POST | User login | Public |
| `/dashboard` | GET | Main dashboard | Required |
| `/dashboard?date=YYYY-MM-DD` | GET | Filtered dashboard | Required |
| `/add` | POST | Create new task | Required |
| `/complete/<id>` | GET | Mark task complete | Required |
| `/uncomplete/<id>` | GET | Mark task incomplete | Required |
| `/edit/<id>` | POST | Update task | Required |
| `/delete/<id>` | GET | Delete task | Required |
| `/logout` | GET | User logout | Required |

---

## 🧪 Testing Checklist

### Manual Testing Performed:

#### User Authentication
- ✅ Register new user with valid data
- ✅ Register with existing username (should fail)
- ✅ Register with invalid email format (should fail)
- ✅ Register with password mismatch (should fail)
- ✅ Login with correct credentials
- ✅ Login with wrong password (should fail)
- ✅ Logout functionality

#### Task Operations
- ✅ Add task with all fields
- ✅ Add task for today
- ✅ Add task for future date
- ✅ Try to add task for past date (should fail)
- ✅ Edit task details
- ✅ Edit task priority
- ✅ Edit task due date
- ✅ Mark today's task as complete
- ✅ Try to mark future task as complete (should fail)
- ✅ Unmark completed task
- ✅ Delete task with confirmation

#### UI/UX
- ✅ Responsive on mobile (375px width)
- ✅ Responsive on tablet (768px width)
- ✅ Responsive on desktop (1920px width)
- ✅ All animations working
- ✅ Flash messages displaying correctly
- ✅ Modal popup functionality
- ✅ Form validations working

#### Date Functionality
- ✅ Calendar date picker working
- ✅ Date filter showing correct tasks
- ✅ Today's tasks section accurate
- ✅ Date validation preventing past dates
- ✅ Future task completion blocked

---

## 📚 Dependencies

### Required Python Packages
```
Flask==3.0.0
Flask-Login==0.6.3
flask-bcrypt==1.0.1
gunicorn==21.2.0
```

### Frontend Dependencies (CDN)
- FontAwesome 6.4.0 (Icons)

---

## 💻 Development Environment

- **IDE:** Visual Studio Code
- **OS:** Windows 11 
- **Python Version:** 3.11.5
- **Browser Testing:** Chrome, Firefox, Safari, Edge

---


## 👤 Author Information

**Your Name**
- **GitHub:** [@Nirupama15](https://github.com/Nirupama15)
- **Email:** nirupamamadakkara@gmail.com


---

## 🙏 Acknowledgments

- **Flask Documentation** - Comprehensive framework documentation
- **FontAwesome** - Beautiful icon library
- **Render** - Easy deployment platform
- **Python Community** - Helpful resources and tutorials
- **Stack Overflow** - Problem-solving assistance

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the **Known Limitations** section above
2. Review the **How to Run Locally** instructions
3. Open an issue on GitHub
4. Contact via email

---

## 📈 Project Statistics

- **Lines of Code:** ~1,500+
- **Templates:** 4 HTML files
- **Routes:** 10 Flask routes
- **Development Time:** ~15 hours
- **Features Implemented:** 20+
- **Responsive Breakpoints:** 4

---

## ✅ Assignment Completion Checklist

### Required Features (All Completed ✅)
- ✅ Flask-based web application
- ✅ Add daily tasks
- ✅ Edit tasks
- ✅ Delete tasks
- ✅ Mark tasks as completed
- ✅ View all tasks in a simple list
- ✅ Hosted on free platform (Render)
- ✅ Public GitHub repository
- ✅ README with instructions

### Bonus Features (All Completed ✅)
- ✅ SQLite database integration
- ✅ Dynamic task display
- ✅ User authentication system
- ✅ Multiple creative features

### Submission Requirements (All Met ✅)
- ✅ Hosted app URL provided
- ✅ GitHub repository link included
- ✅ README explains how to run locally
- ✅ Hosting platform documented
- ✅ Difficulties faced described
- ✅ Extra features documented

---

**Thank you for reviewing my submission! 🎉**

---
