from fastapi import APIRouter
# import sys
# sys.path.append('../../')
from configs.dbs import conn
from models.index import requests
from schemas.index import Requests

user = APIRouter()


@user.get("/")
async def read_data():
    return conn.execute(requests.select()).fetchall()


@user.get("/{student_id}")
async def read_data(student_id: int):
    return conn.execute(requests.select().where(requests.c.student_id == student_id)).fetchall()


@user.post("/")
async def write_data(user: Requests):
    conn.execute(requests.insert().values(
        student_id=user.student_id,
        category=user.category,
        description=user.description,
        status=user.status,
        date=user.date

    ))
    return conn.execute(requests.select()).fetchall()


@user.put("/{Sr_No}")
async def update_data(Sr_No: int, user: Requests):
    conn.execute(requests.update().
        values(
        category=user.category,
        description=user.description,
        status=user.status,
        date=user.date
    ).where(requests.c.Sr_No == Sr_No))

    return conn.execute(requests.select()).fetchall


@user.delete("/{Sr_No}")
async def delete_data(Sr_No: int):
    conn.execute(requests.delete().where(requests.c.Sr_No == Sr_No))
    return conn.execute(requests.select()).fetchall
