from contextlib import asynccontextmanager
import sqlite3
from fastapi import FastAPI, HTTPException
from app.database import get_connection, initialize_database
from app.schemas import StudentCreate, StudentUpdate, StudentResponse
from app import crud
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="Students Database CRUD API",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5501",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Students Database CRUD API is running!"}


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    connection = get_connection()
    try:
        return crud.create_student(connection, student)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")
    finally:
        connection.close()


@app.get("/students", response_model=list[StudentResponse])
def get_students(course: str | None = None, name: str | None = None):
    connection = get_connection()
    try:
        return crud.get_all_students(connection, course, name)
    finally:
        connection.close()


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    connection = get_connection()
    try:
        student = crud.get_student(connection, student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    finally:
        connection.close()


@app.put("/students/{student_id}", response_model=StudentResponse)
def replace_student(student_id: int, student: StudentCreate):
    connection = get_connection()
    try:
        if crud.get_student(connection, student_id) is None:
            raise HTTPException(status_code=404, detail="Student not found")
        updated = StudentUpdate(**student.model_dump())
        return crud.update_student(connection, student_id, updated)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")
    finally:
        connection.close()


@app.patch("/students/{student_id}", response_model=StudentResponse)
def patch_student(student_id: int, student: StudentUpdate):
    if not student.model_fields_set:
        raise HTTPException(status_code=400, detail="Provide a field to update")

    connection = get_connection()
    try:
        if crud.get_student(connection, student_id) is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return crud.update_student(connection, student_id, student)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")
    finally:
        connection.close()


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    connection = get_connection()
    try:
        if not crud.delete_student(connection, student_id):
            raise HTTPException(status_code=404, detail="Student not found")
    finally:
        connection.close()