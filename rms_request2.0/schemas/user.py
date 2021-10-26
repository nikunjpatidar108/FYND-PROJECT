from pydantic import BaseModel
from datetime import date


class Requests(BaseModel):
    student_id: int
    category: str
    description: str
    status: str
    date: date
