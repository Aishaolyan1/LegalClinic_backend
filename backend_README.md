# Legal Clinic - Backend 🏛️

## 📌 Project Description
The backend of the Legal Clinic app provides a Django REST API for managing user registration, login, case handling, and lawyer-client messaging.

---

## 🧠 Purpose of this File
To document how to install, run, and understand the backend architecture for developers and collaborators.

---

## 🛠 Tech Stack
- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (or SQLite default)
- JWT Authentication (`djangorestframework-simplejwt`)

---

## 📦 Features
- Custom user registration for `client` and `lawyer` roles
- Login with JWT token authentication
- Case creation, messaging between users
- Automatic profile creation on signup

---

## 🔗 Frontend Repository
[LegalClinic Frontend](https://github.com/your-username/legalclinic-frontend)

---

## 🌐 API Endpoints

| Method | URL                | Description                     |
|--------|--------------------|---------------------------------|
| POST   | `/users/signup/`   | Register user (client/lawyer)   |
| POST   | `/users/login/`    | User login and JWT token return |
| GET    | `/users/verify/`   | Token refresh / user verify     |
| GET/POST | `/cases/`        | Get or create cases             |
| POST   | `/messages/`       | Send a message to a lawyer      |

---

## 🖼️ ERD Diagram
![ERD](./Screenshot%202025-04-30%20115621.png)

---

## ⚙️ Installation Instructions

1. **Clone repo and install requirements**
```bash
git clone https://github.com/your-username/legalclinic-backend.git
cd legalclinic-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Run server**
```bash
python manage.py migrate
python manage.py runserver
```

3. **Using Docker**
```bash
docker build -t legalclinic-backend .
docker run -p 8000:8000 legalclinic-backend
```

---

## ❄️ IceBox Features (Planned)
- Admin review for cases
- PDF export for cases
- Lawyer specializations & ratings
- Case status filtering
- Email notifications