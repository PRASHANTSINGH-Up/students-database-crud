def create_students_table(connection):
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