from fastapi import FastAPI
from database import create_table, get_connection
from schemas import StudentCreate , StudentUpdate

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Student CRUD API is running!"}


@app.post("/students")
def create_student(student: StudentCreate):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO students
        (name, date_of_birth, email, phone, course, address, enrollment_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            student.name,
            student.date_of_birth,
            student.email,
            student.phone,
            student.course,
            student.address,
            student.enrollment_date
        )
    )
@app.get("/students")
def get_students():
    connection = get_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return [dict(student) for student in students]
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if student is None:
        return {"message": "Student not found"}

    return dict(student)
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    connection = get_connection()

    existing_student = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    ).fetchone()

    if existing_student is None:
        connection.close()
        return {"message": "Student not found"}

    connection.execute(
        """
        UPDATE students
        SET name = ?,
            date_of_birth = ?,
            email = ?,
            phone = ?,
            course = ?,
            address = ?,
            enrollment_date = ?
        WHERE student_id = ?
        """,
        (
            student.name,
            student.date_of_birth,
            student.email,
            student.phone,
            student.course,
            student.address,
            student.enrollment_date,
            student_id
        )
    )
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()

    existing_student = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    ).fetchone()

    if existing_student is None:
        connection.close()
        return {"message": "Student not found"}

    connection.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()

    return {"message": "Student deleted successfully"}

    connection.commit()
    connection.close()

    return {"message": "Student updated successfully"}    

    connection.commit()

    student_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Student created successfully",
        "student_id": student_id
    }