from mongoengine import DateTimeField, Document, EnumField, IntField, StringField

from src.utils import DateTime


class BaseDocument(Document):
    inserted_at = DateTimeField()
    updated_at = DateTimeField()

    def clean(self):
        if not self.inserted_at:
            self.inserted_at = DateTime.current_datetime()
        self.updated_at = DateTime.current_datetime()


class User(BaseDocument):
    id = IntField(required = True)
    name = StringField()
    last_name = StringField()
    identification = IntField()
    identification_type = EnumField(['CC', 'CE', 'TI'])
    rol = StringField()
