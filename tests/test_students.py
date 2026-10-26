import pytest
from fastapi.testclient import TestClient
from app.main import app
import app.main as main
import sqlite3


@pytest.fixture
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test_students.db"

    def get_test_connection():
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                course TEXT NOT NULL,
                address TEXT,
                enrollment_date TEXT NOT NULL
            )
        """)
        connection.commit()
        return connection

    monkeypatch.setattr(main, "get_connection", get_test_connection)
    monkeypatch.setattr(main, "initialize_database", lambda: None)

    with TestClient(app) as test_client:
        yield test_client


def sample_student():
    return {
        "name": "Aman Verma",
        "date_of_birth": "2005-05-15",
        "email": "aman.test@example.com",
        "phone": "9876543210",
        "course": "CSE",
        "address": "Bhopal",
        "enrollment_date": "2026-01-10"
    }


def test_create_student(client):
    response = client.post("/students", json=sample_student())

    assert response.status_code == 201
    assert response.json()["name"] == "Aman Verma"


def test_get_all_students(client):
    client.post("/students", json=sample_student())

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_nonexistent_student(client):
    response = client.get("/students/999")

    assert response.status_code == 404


def test_update_student(client):
    created = client.post("/students", json=sample_student()).json()

    response = client.patch(
        f"/students/{created['id']}",
        json={"name": "Rahul Sharma"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Rahul Sharma"


def test_delete_student(client):
    created = client.post("/students", json=sample_student())

    student_id = created.json()["id"]
    response = client.delete(f"/students/{student_id}")

    assert response.status_code == 204
    assert client.get(f"/students/{student_id}").status_code == 404