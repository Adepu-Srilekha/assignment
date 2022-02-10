from pydantic import BaseModel

class Student(BaseModel):
    __tablename__ = 'student_data'
    name : str
    Telugu : int
    English : int
    Hindi : int
    Science :int
    Maths :int
    Biology :int



