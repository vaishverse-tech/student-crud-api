# Students Database CRUD Application

A simple Student Database CRUD API built using Python, FastAPI, and SQLite.

## Project Overview

This project provides a REST API to manage student records.

The application supports the following CRUD operations:

- Create a student
- Read all students
- Read a single student
- Update student details
- Delete a student

## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

## Student Details

Each student record can contain:

- Student ID
- Name
- Date of Birth
- Email
- Phone
- Course
- Address
- Enrollment Date

## Project Structure

```text
student-crud-api/
│
├── main.py
├── database.py
├── schemas.py
├── students.db
├── requirements.txt
├── README.md
└── venv/