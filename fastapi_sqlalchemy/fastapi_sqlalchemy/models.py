from database import Base
from sqlalchemy import Column, Integer, String


class Student_model(Base):
    __tablename__ = 'student_data'
    stu_id = Column(Integer,primary_key=True)
    name = Column(String)
    Telugu = Column(Integer)
    English = Column(Integer)
    Hindi = Column(Integer)
    Science = Column(Integer)
    Maths = Column(Integer)
    Biology = Column(Integer)
    status = Column(String)
    chance = Column(String)
