# 🎓 Student Management System

A Django-based web application for managing student data with an admin interface.

---

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

### 🖥️ Prerequisites

- Python 3.x installed
- Django installed (`pip install django`)
- Virtual environment (recommended)

---

## ⚙️ Setup Instructions

```bash
# 1. Activate virtual environment
dbms/Scripts/activate

# Or, create and activate a new one (don't include Scripts folder in repo)
# Windows
python -m venv venv
then activate it
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# 2. Navigate to project directory
cd dbms

# 3. (Optional) Run development server to test
python manage.py runserver

# 4. Make migrations
python manage.py makemigrations

# 5. Apply migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser
# Enter your email and password when prompted

# 7. Run the server
python manage.py runserver

# 8 . Visit http://localhost:8000/admin   to see admin pannel

