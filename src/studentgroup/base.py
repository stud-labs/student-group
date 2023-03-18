from json import dumps, loads
from bson.objectid import ObjectId
from .mongoconn import db


class Base:
    def store(self, coll):
        d = {}
        for name in vars(self):
            val = getattr(self, name)
            d[name] = val

        js = dumps(d)
        rc = coll.insert_one(d)
        print(rc)


    def loadattrs(self, json):
        if isinstance(json, dict):
            d = json
        else:
            d = loads(json)
        for name, val in d.items():
            setattr(self, name, val)

    @classmethod
    def new(cls, coll, objid, class_):
        answer = coll.find({"_id":ObjectId(objid)})
        for d in answer:
            i = class_()
            i.loadattrs(d)
        return i

    @classmethod
    def load(cls, db, objid):
        colname = cls.__name__.lower()
        if hasattr(cls, "__collection__"):
            colname = cls.__collection__
        groups = db[colname]
        g = cls.new(groups, objid, cls)
        return g
