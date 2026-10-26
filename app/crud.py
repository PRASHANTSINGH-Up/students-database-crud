from app.schemas import StudentCreate, StudentUpdate


def create_student(connection, student: StudentCreate):
    data = student.model_dump(mode="json")

    columns = ", ".join(data.keys())
    placeholders = ", ".join("?" for _ in data)

    cursor = connection.execute(
        f"INSERT INTO students ({columns}) VALUES ({placeholders})",
        tuple(data.values())
    )

    connection.commit()

    return get_student(connection, cursor.lastrowid)


def get_all_students(connection, course=None, name=None):
    query = "SELECT * FROM students WHERE 1=1"
    params = []

    if course:
        query += " AND course = ?"
        params.append(course)

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")

    query += " ORDER BY id"

    rows = connection.execute(query, params).fetchall()

    return [dict(row) for row in rows]


def get_student(connection, student_id):
    row = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    return dict(row) if row else None


def update_student(connection, student_id, student: StudentUpdate):
    data = student.model_dump(mode="json", exclude_unset=True)

    if not data:
        return get_student(connection, student_id)

    columns = ", ".join(f"{key} = ?" for key in data)

    cursor = connection.execute(
        f"UPDATE students SET {columns} WHERE id = ?",
        (*data.values(), student_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        return None

    return get_student(connection, student_id)


def delete_student(connection, student_id):
    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    return cursor.rowcount > 0