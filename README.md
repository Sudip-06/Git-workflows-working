# 🎓 Placement Portal Application (PPA)

A full-stack campus recruitment platform built with **Flask + Vue 3 + SQLite + Redis + Celery**.

---

## 📋 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend API | Flask 3.x + Flask-JWT-Extended |
| Frontend | Vue 3 (CDN, no CLI needed) + Vue Router 4 |
| Styling | Bootstrap 5.3 + Bootstrap Icons |
| Charts | Chart.js 4 |
| Database | SQLite (programmatically created) |
| Cache | Redis + Flask-Caching |
| Async Jobs | Celery + Redis |
| Auth | JWT tokens |

---

## 🚀 Quick Start

### 1. Prerequisites

```bash
# Ensure these are installed:
python >= 3.10
redis-server
```

### 2. Install Dependencies

```bash
cd placement-portal
pip install -r requirements.txt
```

### 3. Start Redis

```bash
# Linux/Mac
redis-server

# Windows (WSL or Redis for Windows)
redis-server --daemonize yes
```

### 4. Run Flask Backend

```bash
python run.py
# Server starts at http://localhost:5000
# Admin is auto-seeded: admin@ppa.edu / Admin@123
```

### 5. Start Celery Worker (for async jobs)

```bash
# In a separate terminal:
celery -A celery_worker.celery worker --loglevel=info
```

### 6. Start Celery Beat (for scheduled jobs)

```bash
# In a third terminal:
celery -A celery_worker.celery beat --loglevel=info
```

### 7. Open the App

Visit `http://localhost:5000` in your browser.

---

## 👤 Demo Accounts

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@ppa.edu | Admin@123 |
| Company | Register via UI | — |
| Student | Register via UI | — |

---

## 🏗️ Project Structure

```
placement-portal/
├── run.py                    # Flask entry point
├── celery_worker.py          # Celery worker entry point
├── config.py                 # App configuration
├── requirements.txt
├── app/
│   ├── __init__.py           # App factory + DB init
│   ├── models.py             # SQLAlchemy models (auto-creates DB)
│   ├── auth/routes.py        # Login, Register, Me
│   ├── admin/routes.py       # Admin dashboard + management
│   ├── company/routes.py     # Company profile + drives + applicants
│   ├── student/routes.py     # Student profile + drives + applications
│   └── jobs/tasks.py         # Celery tasks (reminders, reports, CSV, offer letter)
├── templates/
│   └── index.html            # Jinja2 CDN entry point for Vue SPA
└── static/
    ├── js/app.js             # Complete Vue 3 SPA
    └── uploads/              # Resume and file uploads
```

---

## ✨ Features Implemented

### 🔐 Authentication
- [x] JWT-based auth for all roles
- [x] Role-based access control (Admin / Company / Student)
- [x] Admin pre-seeded programmatically
- [x] Password hashing (Werkzeug)
- [x] Protected routes (frontend + backend)

### 🏛️ Admin
- [x] Dashboard with stats + Chart.js charts
- [x] Approve / Reject / Blacklist companies
- [x] Approve / Reject / Close drives
- [x] Deactivate/activate students and companies
- [x] View all applications with funnel chart
- [x] Monthly placement reports
- [x] Export all applications as CSV (async)
- [x] Search companies, students, drives

### 🏢 Company
- [x] Register + await admin approval
- [x] Full company profile management
- [x] Create / Edit / Delete placement drives
- [x] 13-field drive form (title, salary, branches, CGPA, deadline, etc.)
- [x] View applicants per drive with status update
- [x] Interview feedback system (communication, technical, recommendation)
- [x] Interview slot creation + management
- [x] Export applicants as CSV (async)
- [x] Offer letter generator (HTML, async)
- [x] Notifications panel

### 🎓 Student
- [x] Register + full profile management
- [x] Profile completion meter (checklist + % bar)
- [x] Resume upload (PDF/DOC/DOCX)
- [x] Browse approved drives with ATS score per drive
- [x] Intelligent eligibility engine (branch, CGPA, year, deadline)
- [x] Smart drive recommendations (rule-based)
- [x] Apply with duplicate + eligibility guard
- [x] Track application status with progress bar
- [x] Application history timeline
- [x] Interview slot booking
- [x] View interview feedback from company
- [x] Export CSV (async, notified when done)
- [x] Notifications panel

### ⚡ Performance
- [x] Redis caching (approved drives list, admin dashboard)
- [x] Cache invalidation on status changes
- [x] Cache expiry configured

### 📬 Background Jobs
- [x] Daily reminder job (deadlines, interview tomorrow)
- [x] Monthly report job (HTML email to admin)
- [x] CSV export jobs (student, company, admin)
- [x] Offer letter generation job
- [x] Celery Beat schedules

### 📊 Analytics / Charts
- [x] Admin: monthly application trend (line chart)
- [x] Admin: department-wise placements (doughnut)
- [x] Admin: application funnel (bar chart)
- [x] Company: applicant funnel (bar chart)
- [x] Student: status breakdown (doughnut)

---

## 🔑 Key API Endpoints

```
POST /api/auth/login
POST /api/auth/register
GET  /api/auth/me

GET  /api/admin/dashboard
GET  /api/admin/companies
PUT  /api/admin/companies/:id/status
GET  /api/admin/students
PUT  /api/admin/students/:id/status
GET  /api/admin/drives
PUT  /api/admin/drives/:id/status

GET  /api/company/dashboard
GET  /api/company/profile
POST /api/company/drives
GET  /api/company/drives/:id/applicants
PUT  /api/company/applications/:id
POST /api/company/drives/:id/slots
POST /api/company/applications/:id/offer-letter

GET  /api/student/drives
POST /api/student/drives/:id/apply
GET  /api/student/applications
GET  /api/student/recommendations
POST /api/student/export/csv
```

---

## 📝 Environment Variables (optional)

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
REDIS_URL=redis://localhost:6379/0
ADMIN_EMAIL=admin@ppa.edu
ADMIN_PASSWORD=Admin@123
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your@gmail.com
MAIL_PASSWORD=your-app-password
```

---

## 📌 Notes

- The database (`placement_portal.db`) is auto-created on first run via SQLAlchemy `db.create_all()`
- No manual DB creation (DB Browser etc.) is used — fulfills the project requirement
- All file uploads stored in `static/uploads/`
- Vue 3 SPA loaded via single Jinja2 template (`templates/index.html`) — CDN only, no CLI
