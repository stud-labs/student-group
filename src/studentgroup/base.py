from json import dumps, loads
from bson.objectid import ObjectId
from .mongoconn import db


class Base:

    def insert(self):
        d = {}
        for name in vars(self):
            val = getattr(self, name)
            d[name] = val
        coll = self.__class__.collection()
        rc = coll.insert_one(d)
        return rc.inserted_id

    def loadattrs(self, json):
        if isinstance(json, dict):
            d = json
        else:
            d = loads(json)
        for name, val in d.items():
            setattr(self, name, val)

    def update(self, objid, json):
        self.loadattrs(json)
        newvalues = {"$set": json}
        coll = self.__class__.collection()
        coll.update_one({"_id": ObjectId(objid)}, newvalues)

    @classmethod
    def new(cls, coll, objid, class_):
        answer = coll.find({"_id": ObjectId(objid)})
        for d in answer:
            i = class_()
            i.loadattrs(d)
        return i

    @classmethod
    def load(cls, db, objid):
        coll = cls.collection()
        g = cls.new(coll, objid, cls)
        return g

    @classmethod
    def list(cls):
        coll = cls.collection()
        l = []
        for e in coll.find({}):
            i = cls()
            i.loadattrs(e)
            l.append((e["_id"], i))
        return l

    @classmethod
    def collection(cls):
        colname = cls.__name__.lower()
        if hasattr(cls, "__collection__"):
            colname = cls.__collection__
        return db[colname]
