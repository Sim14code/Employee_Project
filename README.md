# Employee Management System

## Project Overview

The Employee Management System is a Django-based application designed to manage employees, departments, attendance, and performance data. It provides RESTful APIs for CRUD operations, includes filtering and pagination, and optionally visualizes data using charts.

---

## Features

1. **Employee Management**:

   - Create, Read, Update, and Delete (CRUD) operations for employees.
   - Assign employees to specific departments.

2. **Attendance Management**:

   - Track employee attendance (Present/Absent/Late).

3. **Performance Tracking**:

   - Record employee performance ratings.

4. **APIs**:

   - Expose RESTful APIs with pagination and filtering.
   - Authentication using Simple JWT.

5. **Swagger Documentation**:

   - Explore APIs via Swagger UI.

6. **Optional Docker Support**:

   - Run the application in a containerized environment.

---

## Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Database**: PostgreSQL
- **Tools**: drf-yasg, django-environ, Faker, psycopg2-binary

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

- Create a `.env` file in the project root and add the following:

```env
DATABASE_URL="postgres://<user>:<password>@localhost:5432/<database>"
```

### 5. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed the Database with Dummy Data

```bash
python manage.py seed_data
```

### 7. Run the Application

```bash
python manage.py runserver
```

- The application will be available at `http://127.0.0.1:8000/`.

### 8. Access Swagger Documentation

- Visit `http://127.0.0.1:8000/swagger/` to explore the API documentation.

---

## API Endpoints

### Employee APIs

- **GET** `/api/employees/` - List all employees (with pagination).
- **POST** `/api/employees/` - Create a new employee.
- **GET** `/api/employees/<id>/` - Retrieve employee details.
- **PUT** `/api/employees/<id>/` - Update an employee.
- **DELETE** `/api/employees/<id>/` - Delete an employee.

### Department APIs

- **GET** `/api/departments/`
- **POST** `/api/departments/`

### Attendance APIs

- **GET** `/api/attendance/`
- **POST** `/api/attendance/`

### Performance APIs

- **GET** `/api/performance/`
- **POST** `/api/performance/`

---

## File Structure

```plaintext
employee-management-system/
├── employees/
├── attendance/
├── performance/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Author

**Simar Ahluwalia**
