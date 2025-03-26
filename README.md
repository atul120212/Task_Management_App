# Task Management API

## Project Overview
This is a Task Management API built using **Django** and **Django Rest Framework (DRF)**. It allows users to create tasks, assign tasks to specific users, and retrieve tasks assigned to a particular user.

## Features
- Create tasks
- Assign tasks to users
- Retrieve tasks assigned to a user

## Tech Stack
- **Backend:** Django, Django Rest Framework (DRF)
- **Database:** SQLite (default), can be switched to PostgreSQL/MySQL
- **Authentication:** Token-based authentication (can be extended to JWT)

---

## Installation and Setup

### 1. Clone the Repository
```bash
$ git clone <repository_url>
$ cd task_management_api
```

### 2. Create a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. Create a Superuser (Admin User)
```bash
$ python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

### 6. Run the Development Server
```bash
$ python manage.py runserver
```

Now, the API will be available at `http://127.0.0.1:8000/`

---

## API Endpoints

### 1. Register a New User
**Endpoint:** `POST /api/register/`
```json
{
    "username": "atul",
    "name": "Atul Sharma",
    "email": "atul@example.com",
    "mobile": "9876543210",
    "password": "securepassword"
}
```

**Response:**
```json
{
    "id": 1,
    "username": "atul",
    "name": "Atul Sharma",
    "email": "atul@example.com",
    "mobile": "9876543210"
}
```

---

### 2. Create a Task
**Endpoint:** `POST /api/tasks/`
```json
{
    "name": "Complete UI Development",
    "description": "Implement all required UI components.",
    "task_type": "work",
    "status": "pending"
}
```

**Response:**
```json
{
    "id": 4,
    "assigned_users": [],
    "name": "Complete UI Development",
    "description": "Implement all required UI components.",
    "created_at": "2025-03-26T05:58:12.407257Z",
    "task_type": "work",
    "completed_at": null,
    "status": "pending"
}
```

---

### 3. Assign Task to Users
**Endpoint:** `POST /api/tasks/<task_id>/assign/`
```json
{
    "emails": ["john.doe@example.com", "johny.doe@example.com"]
}
```

**Response:**
```json
{
    "id": 4,
    "assigned_users": [
        {
            "id": 2,
            "name": "John",
            "email": "john.doe@example.com"
        },
        {
            "id": 3,
            "name": "Johny",
            "email": "johny.doe@example.com"
        }
    ],
    "name": "Complete UI Development",
    "description": "Implement all required UI components.",
    "created_at": "2025-03-26T05:58:12.407257Z",
    "task_type": "work",
    "completed_at": null,
    "status": "pending"
}
```

---

### 4. Get Tasks Assigned to a User
**Endpoint:** `GET /api/user/<user_id>/tasks/`

**Response:**
```json
[
    {
        "id": 1,
        "name": "Complete Development",
        "description": "Implement all required.",
        "created_at": "2025-03-26T04:04:47.753896Z",
        "task_type": "personal",
        "completed_at": null,
        "status": "completed"
    },
    {
        "id": 2,
        "name": "Complete UI Development",
        "description": "Implement all required UI.",
        "created_at": "2025-03-26T05:03:09.572867Z",
        "task_type": "work",
        "completed_at": null,
        "status": "pending"
    }
]
```

---

## Running Tests
Run the following command to execute tests:
```bash
$ python manage.py test
```

---

## Future Enhancements
- JWT authentication for better security
- Pagination for task lists
- WebSockets for real-time task updates
- Frontend integration (React or Vue.js)

## Author
**Atul Sharma**

