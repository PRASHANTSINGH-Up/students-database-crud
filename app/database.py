import sqlite3
from pathlib import Path

DATABASE_NAME = Path(__file__).resolve().parent.parent / "students.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    from app.models import create_students_table

    connection = get_connection()

    try:
        create_students_table(connection)
    finally:
        connection.close()