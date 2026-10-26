# Students Database CRUD Application

A web-based Student Management System built using Python, FastAPI, SQLite, HTML, CSS, and JavaScript. The application allows users to manage student records through a responsive dashboard and RESTful API.

## Features

* **Create Student:** Add new student records.
* **View Students:** View all students and individual student details.
* **Update Student:** Modify existing student information.
* **Delete Student:** Remove student records.
* **Search Students:** Search students by name.
* **Filter Students:** Filter records by course.
* **Data Validation:** Validate input using Pydantic.
* **Duplicate Email Prevention:** Prevent duplicate email addresses.
* **SQLite Database:** Store student records persistently.
* **REST API:** Perform CRUD operations through API endpoints.
* **Automated Testing:** Test important API operations using pytest.

## Technology Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Backend programming           |
| FastAPI        | REST API development          |
| SQLite         | Database management           |
| Pydantic       | Data validation               |
| HTML5          | Frontend structure            |
| CSS3           | Styling and responsive layout |
| JavaScript     | Frontend functionality        |
| Uvicorn        | Backend server                |
| pytest         | Automated testing             |
| HTTPX          | API testing support           |
| Git and GitHub | Version control               |

## Project Structure

```text
students-database-crud/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── tests/
│   └── test_students.py
│
├── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

Install the following before running the project:

* Python 3.10 or later
* Git
* Visual Studio Code
* A modern web browser
* VS Code Live Server extension

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PRASHANTSINGH-Up/students-database-crud.git
```

### 2. Navigate to the Project Directory

```bash
cd students-database-crud
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Application

### Start the Backend

Run the following command from the project root:

```bash
python -m uvicorn app.main:app --reload
```

The backend server will start at:

`http://127.0.0.1:8000`

### Open API Documentation

Visit the following URL in your browser:

`http://127.0.0.1:8000/docs`

FastAPI provides interactive API documentation through Swagger UI.

### Start the Frontend

1. Open the project folder in Visual Studio Code.
2. Right-click `index.html`.
3. Select **Open with Live Server**.

The frontend will typically open at:

`http://127.0.0.1:5500/index.html`

Keep the backend server running while using the frontend.

## API Endpoints

| Method | Endpoint                 | Description                      |
| ------ | ------------------------ | -------------------------------- |
| GET    | `/`                      | Check API status                 |
| POST   | `/students`              | Create a student                 |
| GET    | `/students`              | Retrieve all students            |
| GET    | `/students/{student_id}` | Retrieve a student by ID         |
| PUT    | `/students/{student_id}` | Replace student details          |
| PATCH  | `/students/{student_id}` | Partially update student details |
| DELETE | `/students/{student_id}` | Delete a student                 |

### Search and Filter

**Search by name:**

```http
GET /students?name=Aman
```

**Filter by course:**

```http
GET /students?course=CSE
```

**Combine search and filtering:**

```http
GET /students?course=CSE&name=Aman
```

### Example: Create a Student

**Request:** `POST /students`

**JSON Body:**

```json
{
  "name": "Aman Verma",
  "date_of_birth": "2005-05-15",
  "email": "aman@example.com",
  "phone": "9876543210",
  "course": "CSE",
  "address": "Bhopal",
  "enrollment_date": "2026-01-10"
}
```

A successful request returns the created student record along with its generated ID.

## Database Schema

The application uses SQLite and creates a table named `students`.

| Field             | Data Type | Description                        |
| ----------------- | --------- | ---------------------------------- |
| `id`              | INTEGER   | Primary key with auto-increment    |
| `name`            | TEXT      | Student's name                     |
| `date_of_birth`   | TEXT      | Student's date of birth            |
| `email`           | TEXT      | Unique email address when provided |
| `phone`           | TEXT      | Contact number                     |
| `course`          | TEXT      | Student's course                   |
| `address`         | TEXT      | Residential address                |
| `enrollment_date` | TEXT      | Enrollment date                    |

Dates are stored in `YYYY-MM-DD` format.

The database table is initialized automatically when the backend starts.

## Error Handling and Validation

The application handles common errors using appropriate HTTP status codes.

| Status Code | Description                    |
| ----------- | ------------------------------ |
| 201         | Student created successfully   |
| 200         | Request completed successfully |
| 204         | Student deleted successfully   |
| 400         | Invalid update request         |
| 404         | Student not found              |
| 409         | Duplicate email address        |
| 422         | Input validation failed        |

Pydantic validates incoming data, and parameterized SQL queries are used for database operations.

## Automated Testing

The project uses pytest and FastAPI TestClient to test API functionality.

Run the tests using:

```bash
python -m pytest tests/ -v
```

### Tests Included

* Creating a student
* Retrieving all students
* Handling nonexistent student IDs
* Updating student information
* Deleting a student

The current test suite contains five tests, all of which passed during the last test run.

## Future Improvements

* GitHub Actions for automated testing
* Pagination for student records
* User authentication and authorization
* Additional automated test cases
* Deployment to a public hosting platform
* Improved frontend notifications and validation

## Author

**Prashant Singh**

GitHub: [PRASHANTSINGH-Up](https://github.com/PRASHANTSINGH-Up)

**Project Repository:** [Students Database CRUD Application](https://github.com/PRASHANTSINGH-Up/students-database-crud)
