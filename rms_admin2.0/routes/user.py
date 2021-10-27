from fastapi import APIRouter
from configs.dbs import conn
from models.index import admin
from schemas.index import Admin
from models.index import requests
from schemas.index import Requests

user = APIRouter()

@user.get("/get-log-request")
async def read_data():
    return conn.execute(requests.select()).fetchall()


@user.get("/get-request-by-student_id/{student_id}")
async def read_data(student_id: int):
    return conn.execute(requests.select().where(requests.c.student_id == student_id)).fetchall()


@user.put("/change-status-of-requests/{Sr_No}")
async def update_data(Sr_No: int, user: Requests):
    conn.execute(requests.update().
        values(
        status=user.status,
        date=user.date
    ).where(requests.c.Sr_No == Sr_No))

    return conn.execute(requests.select()).fetchall()

# @user.get("/")
# async def read_data():
#     return conn.execute(admin.select()).fetchall()


# @user.get("/{admin_id}")
# async def read_data(admin_id: int):
#     return conn.execute(admin.select().where(admin.c.admin_id == admin_id)).fetchall()


# @user.post("/")
# async def write_data(user: Admin):
#     conn.execute(admin.insert().values(
#         admin_id=user.admin_id,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         gender=user.gender,
#         password=user.password
#
#     ))
#     return conn.execute(admin.select()).fetchall()


# @user.put("/{admin_id}")
# async def update_data(admin_id: int, user: Admin):
#     conn.execute(admin.update().
#         values(
#         first_name=user.first_name,
#         last_name=user.last_name,
#         gender=user.gender,
#         password=user.password
#     ).where(admin.c.admin_id == admin_id))
#
#     return conn.execute(admin.select()).fetchall


# @user.delete("/{admin_id}")
# async def delete_data(admin_id: int):
#     conn.execute(admin.delete().where(admin.c.admin_id == admin_id))
#     return conn.execute(admin.select()).fetchall
