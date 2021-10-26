from pydantic import BaseModel
from datetime import date


class Admin(BaseModel):
    admin_id: int
    first_name: str
    last_name: str
    gender: str
    password: str


class Requests(BaseModel):
    # student_id: int
    # category: str
    # description: str
    status: str
    date: date