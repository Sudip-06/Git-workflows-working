# Placement Portal Application (PPA)

Placement Portal Application is a full-stack campus recruitment system built with Flask, Vue 3, SQLite, Redis, and Celery.

## Tech stack

- Backend: Flask, Flask-JWT-Extended, SQLAlchemy
- Frontend: Vue 3, Vue Router, Bootstrap 5
- Database: SQLite
- Cache and broker: Redis
- Background jobs: Celery + Celery Beat
- Notifications: In-app notifications, Gmail SMTP, Google Chat webhook, optional Twilio SMS

## Included files

- `run.py` — Flask app entry point
- `celery_worker.py` — Celery worker/beat entry point
- `config.py` — configuration
- `requirements.txt` — Python dependencies
- `openapi.yaml` — API definition YAML file
- `app/` — backend modules
- `static/js/app.js` — frontend SPA
- `templates/index.html` — Vue entry page
- `placement_portal.db` — SQLite database file
- `.env.example` — example environment file

## How to run

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Fresh database recommended after this update

This optimized build adds database indexes and the `delivery_logs` table.
If you are updating an older copy of the project, either:

```bash
rm -f placement_portal.db
```

then restart the app so SQLAlchemy can recreate the database, or create the missing table/indexes manually.

### 3. Configure environment variables

Create `.env` in the project root by copying `.env.example`.

```bash
cp .env.example .env
```

Then update values such as:
- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `REDIS_URL`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `MAIL_DEFAULT_SENDER`
- `GCHAT_WEBHOOK_URL`
- `REMINDER_TIME`

### 4. Start Redis

On WSL/Linux:

```bash
sudo service redis-server start
redis-cli ping
```

Expected result:

```bash
PONG
```

### 5. Run Flask app

```bash
python run.py
```

The app runs at:

```text
http://localhost:5000
```

Default seeded admin:

```text
admin@ppa.edu / Admin@123
```

### 6. Run Celery worker

Open a second terminal:

```bash
source venv/bin/activate
celery -A celery_worker.celery worker --loglevel=info
```

### 7. Run Celery Beat

Open a third terminal:

```bash
source venv/bin/activate
celery -A celery_worker.celery beat --loglevel=info
```




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

## Main API endpoints

### Auth
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

### Student
- `GET /api/student/drives`
- `GET /api/student/drives/<id>`
- `POST /api/student/drives/<id>/apply`
- `GET /api/student/applications`
- `POST /api/student/applications/<id>/book-slot`
- `GET /api/student/recommendations`

### Company
- `GET /api/company/dashboard`
- `GET /api/company/drives`
- `POST /api/company/drives`
- `GET /api/company/drives/<id>/applicants`
- `POST /api/company/drives/<id>/slots`
- `PUT /api/company/applications/<id>`

### Admin
- `GET /api/admin/dashboard`
- `GET /api/admin/students`
- `GET /api/admin/companies`
- `GET /api/admin/drives`
- `PUT /api/admin/drives/<id>/status`



## Submission note

For final submission, zip the full project folder containing:
- this PDF report
- code folder with all files
- `README.md`
- `api.yaml`


