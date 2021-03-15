from mongoengine import DateTimeField, Document, IntField, StringField

from src.utils import DateTime


class BaseDocument(Document):
    inserted_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {'abstract': True, 'strict': False}

    def clean(self):
        if not self.inserted_at:
            self.inserted_at = DateTime.current_datetime()
        self.updated_at = DateTime.current_datetime()


class Client(BaseDocument):
    name = StringField()
    last_name = StringField()
    identification = IntField(required=True, unique=True)
    identification_type = StringField(required=True)
    rol = StringField()


class User(BaseDocument):
    username = IntField(required=True, unique=True)
    password = StringField(required=True)
