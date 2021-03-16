from datetime import datetime
from unittest import TestCase

from bson import ObjectId
from mongoengine import Document, StringField
from ujson import loads

from src.utils import BsonEncoder
from src.utils.encoder import BsonObject


def res_path(path: str):
    source = 'src.utils.encoder'
    return ".".join([source, path])


class BsonEncoderTestCase(TestCase):

    def test_encode_datetime(self):
        date = datetime(2020, 12, 24, 19, 32)
        example_dict = {
            'date': date
        }

        result = BsonEncoder().encode(example_dict)
        self.assertIsInstance(result, str)

        result_data = loads(result)
        self.assertEqual(result_data.get('date'), date.isoformat())

    def test_encode_bson(self):
        bson_id = "6050084b7948de4c73bd2c1a"
        example_dict = {
            'id': ObjectId(bson_id)
        }

        result = BsonEncoder().encode(example_dict)
        self.assertIsInstance(result, str)
        result_data = loads(result)
        self.assertEqual(result_data.get('id'), bson_id)

    def test_encode_any(self):
        example_dict = {
            'any': 'test',
            'number': 121,
            'in': 12.1,
        }

        result = BsonEncoder().encode(example_dict)
        self.assertIsInstance(result, str)

        result_data = loads(result)
        self.assertEqual(result_data.get('any'), example_dict.get('any'))
        self.assertEqual(result_data.get('number'), example_dict.get('number'))
        self.assertEqual(result_data.get('in'), example_dict.get('in'))


class BsonObjectTestCase(TestCase):

    def setUp(self):
        class AnyDocument(Document):
            name = StringField()
            is_deleted = StringField()

        self.document = AnyDocument(
            name='David',
            is_deleted='Yep'
        )

    def test_to_dict(self):
        assert_dict = dict(name = self.document.name)

        result = BsonObject.to_dict(self.document)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, assert_dict)
