from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date
from configs.dbs import meta

requests = Table(
    'requests', meta,
    Column('student_id', Integer, ForeignKey('student.student_id'), nullable=False),
    # Column('student_id', Integer, ForeignKey('student.student_id'), ondelete='CASCADE', nullable=False),
    Column('category', String(255)),
    Column('description', String(500)),
    Column('status', String(255)),
    Column('date', Date),
)

admin = Table(
    'admin', meta,
    Column('admin_id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('gender', String(255)),
    Column('password', String(255))
)