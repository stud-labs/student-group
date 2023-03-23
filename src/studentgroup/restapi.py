from cornice import Service
from .group import Group
from .student import Student
from .mongoconn import db

group = Service(name='group', path='/api/group/{id}', description="Group API")

groups = Service(name='groups', path='/api/groups', description="Group inserting API")


def _group(request):
    objid = request.matchdict['id']
    g = Group.load(db, objid)
    return g, objid


@group.get()
def get_group(request):
    """Returns json.
    """
    g, objid = _group(request)
    d = {"id": objid, 'name': g.name, 'code': g.code}
    return d


@group.post()
def post_group_data(request):
    g, objid = _group(request)
    js = request.json_body
    g.update(objid, js)

    d = {"id": objid, 'name': g.name, 'code': g.code}
    return d


@groups.put()
def put_group(request):
    js = request.json_body
    g = Group(**js)
    objid = g.insert()
    d = {"id": str(objid), 'name': g.name, 'code': g.code}
    return d
