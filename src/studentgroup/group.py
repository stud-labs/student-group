from .base import Base


class Group(Base):
    __collection__ = "group"

    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code

    def students(self):
        """Return list of students"""
