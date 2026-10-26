# Students Database CRUD Application

A student management application built using Python, FastAPI, SQLite, HTML, CSS, and JavaScript. It allows users to manage student records through a web-based dashboard and REST API.

## Features

* Add new student records
* View all students and individual student details
* Update existing student information
* Delete student records
* Search students by name
* Filter students by course
* Validate input data
* Prevent duplicate email addresses
* Store records persistently using SQLite
* Interactive web-based dashboard

## Technologies Used

* **Backend:** Python, FastAPI
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript
* **API Testing:** FastAPI Swagger UI
* **Version Control:** Git and GitHub

## Project Structure

```text
students-database-crud/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── index.html
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd students-database-crud
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install fastapi uvicorn email-validator
```

### 5. Start the Backend Server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

### 6. Open the API Documentation

Visit:

`http://127.0.0.1:8000/docs`

Use the interactive Swagger UI to test the API endpoints.

### 7. Run the Frontend

Open `index.html` using the VS Code Live Server extension.

The frontend communicates with the FastAPI backend running on `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| POST   | `/students`              | Create a student               |
| GET    | `/students`              | Retrieve all students          |
| GET    | `/students/{student_id}` | Retrieve a student by ID       |
| PUT    | `/students/{student_id}` | Replace student information    |
| PATCH  | `/students/{student_id}` | Update selected student fields |
| DELETE | `/students/{student_id}` | Delete a student               |

## Database

The application uses SQLite to store student records. The database is initialized automatically when the FastAPI application starts.

## Future Improvements

* User authentication and authorization
* Pagination for large student lists
* Improved error handling and logging
* Automated tests
* Deployment to a cloud platform

## Author

Add your name here.
