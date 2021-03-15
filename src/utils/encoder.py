from datetime import datetime
from json import JSONEncoder

from bson import ObjectId
from mongoengine import Document
from ujson import loads


class BsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()
        return JSONEncoder.default(self, o)


class BsonObject:

    @staticmethod
    def to_dict(document: Document):
        raw = BsonEncoder().encode(document.to_mongo())
        document = loads(raw)
        fields = ['_id']
        for key in document.copy().keys():
            if key in fields:
                del document[key]
        return document
