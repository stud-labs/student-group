from .student import Student
from .group import Group
from .mongoconn import db


class TestStudentGroup:
    def test_group_store(self):
        group = db["group"]
        g = Group("Name", 1234)
        g.store(group)

    def test_gen_instance(self):

        objid = '6402bd14a635084ac191cb6b'
        g = Group.load(db,  objid)
        print("Loaded obj:", g)
        pass
