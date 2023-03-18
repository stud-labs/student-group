from cornice import Service
from .group import Group
from .student import Student
from .mongoconn import db

groups = Service(name='group', path='/api/group/{id}', description="Group API")


@groups.get()
def get_value(request):
    """Returns json.
    """
    objid = request.matchdict['id']
    g = Group.load(db, objid)
    d = {
        "id": objid,
        'name': g.name,
        'code': g.code
    }
    return d
