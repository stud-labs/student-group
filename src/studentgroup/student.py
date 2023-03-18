# Student
from .base import Base


class Student(Base):
    def __init__(self, name, code, group):
        self.name = name
        self.code = code
        self.group = group
