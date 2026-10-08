
A simple Student Database CRUD API built using Python, FastAPI, and SQLite.

## Project Overview

This project provides a REST API to manage student records.



## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

## Student Details

- Student ID
- Name
- Date of Birth
- Email
- Phone
- Course
- Address
- Enrollment Date

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /students | Create a student |
| GET | /students | Get all students |
| GET | /students/{student_id} | Get a single student |
| PUT | /students/{student_id} | Update a student |
| DELETE | /students/{student_id} | Delete a student |

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
Run the application:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

