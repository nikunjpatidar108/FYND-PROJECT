from fastapi import APIRouter
from configs.dbs import conn
from models.index import student
from schemas.index import Student
from models.index import requests
from schemas.index import Requests

user = APIRouter()


# this is get method of requests from request database by student_id
@user.get("/get-request-by-student_id/{student_id}")
async def read_data(student_id: int):
    return conn.execute(requests.select().where(requests.c.student_id == student_id)).fetchall()


@user.get("/get-log-request")
async def read_data():
    return conn.execute(requests.select()).fetchall()


@user.put("/change-status-of-requests/{Sr_No}")
async def update_data(Sr_No: int, user: Requests):
    conn.execute(requests.update().
        values(
        status=user.status,
        date=user.date
    ).where(requests.c.Sr_No == Sr_No))

    return conn.execute(requests.select()).fetchall()


# this is post method of requests to log request in request database
@user.post("/insert-requests")
async def write_data(user: Requests):
    conn.execute(requests.insert().values(
        student_id=user.student_id,
        category=user.category,
        description=user.description,
        status=user.status,
        date=user.date
    ))
    return conn.execute(requests.select()).fetchall()


# this is get method of student to get all data of students
@user.get("/get-all-student-data")
async def read_data_student():
    return conn.execute(student.select()).fetchall()


# this is get method of student data from student database by student_id
@user.get("/get-data-by-student_id/{student_id}")
async def read_data(student_id: int):
    return conn.execute(student.select().where(student.c.student_id == student_id)).fetchall()


# this is post method of student to insert data in student database
@user.post("/insert-student-data")
async def write_data(user: Student):
    conn.execute(student.insert().values(
        student_id=user.student_id,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        password=user.password,
        room_no=user.room_no

    ))
    return conn.execute(student.select()).fetchall()


# this is put method of student to update student data by student_id
@user.put("/update-student-details/{student_id}")
async def update_data(student_id: int, user: Student):
    conn.execute(student.update().
        values(
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        password=user.password,
        room_no=user.room_no
    ).where(student.c.student_id == student_id))

    return conn.execute(student.select()).fetchall


# this is delete method of student to delete data of student by student_ID
@user.delete("/delete-by-student_id/{student_id}")
async def delete_data(student_id: int):
    conn.execute(student.delete().where(student.c.student_id == student_id))
    return conn.execute(student.select()).fetchall
