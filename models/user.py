from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date
from configs.dbs import meta

student = Table(
    'student', meta,
    Column('student_id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('gender', String(255)),
    Column('password', String(255)),
    Column('room_no', String(255))
)

requests = Table(
    'requests', meta,
    Column('student_id', Integer, ForeignKey('student.student_id'), nullable=False),
    # Column('student_id', Integer, ForeignKey('student.student_id'), ondelete='CASCADE', nullable=False),
    Column('category', String(255)),
    Column('description', String(500)),
    Column('status', String(255)),
    Column('date', Date),
    Column('Sr_No', Integer, nullable=False, autoincrement=True, primary_key=True)
)
