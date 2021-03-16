from unittest import TestCase

from mongoengine import connect, disconnect

from src.business.client import (
    ClientResponse,
    CreateClient,
    DeleteClient,
    FindClient,
    UpdateClient
)
from src.models import Client, ClientInput, ClientUpdateInput
from src.models.db_models.client import User
from src.utils import ClientMessages, UserMessages


class CreateClientTestCase(TestCase):

    def setUp(self):
        connect('mongoenginetest', host='mongomock://localhost')
        self.client_a = Client(
            identification=123456789,
            identification_type='CC'
        )
        self.client_a.save()
        self.client_b = Client(
            identification = 9876,
            identification_type = 'CC'
        )
        self.client_b.save()
        self.user_a = User(
            username=self.client_a.identification,
            password='A1B2C3'
        )
        self.user_a.save()
        self.use_case = CreateClient()

    def tearDown(self):
        disconnect()

    def test_handle_success(self):
        input_client = ClientInput(
            name='name client',
            last_name='last_name client',
            identification=12345,
            identification_type='CC',
            rol='boss',
            password='my_password'
        )

        result = self.use_case.handle(input_client)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.message, ClientMessages.CREATED)

    def test_handle_user_exist(self):
        input_client = ClientInput(
            name='name client',
            last_name='last_name client',
            identification=123456789,
            identification_type='CC',
            rol='boss',
            password='my_password'
        )

        result = self.use_case.handle(input_client)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.message, UserMessages.EXIST)

    def test_handle_client_exist(self):
        input_client = ClientInput(
            name='name client',
            last_name='last_name client',
            identification=9876,
            identification_type='CC',
            rol='boss',
            password='my_password'
        )

        result = self.use_case.handle(input_client)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.message, ClientMessages.EXIST)


class FindClientTestCase(TestCase):

    def setUp(self):
        connect('mongoenginetest', host='mongomock://localhost')
        self.client_a = Client(
            identification = 123456789,
            identification_type = 'CC'
        )
        self.client_a.save()
        self.user_a = User(
            username = self.client_a.identification,
            password = 'A1B2C3'
        )
        self.user_a.save()
        self.use_case = FindClient()

    def tearDown(self):
        disconnect()

    def test_handle_success(self):
        client_id = 123456789

        result = self.use_case.handle(client_id)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.message, ClientMessages.FOUND)

    def test_handle_not_found(self):
        client_id = 1234

        result = self.use_case.handle(client_id)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(result.message, ClientMessages.NOT_FOUND)


class UpdateClientTestCase(TestCase):

    def setUp(self):
        connect('mongoenginetest', host = 'mongomock://localhost')
        self.client_a = Client(
            identification = 123456789,
            identification_type = 'CC'
        )
        self.client_a.save()
        self.user_a = User(
            username = self.client_a.identification,
            password = 'A1B2C3'
        )
        self.user_a.save()
        self.use_case = UpdateClient()

    def tearDown(self):
        disconnect()

    def test_handle_success(self):
        client_id = 123456789
        client = ClientUpdateInput(
            name='Jose',
            last_name='Cuervo',
            rol='admin'
        )
        result = self.use_case.handle(client_id, client)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.message, ClientMessages.UPDATED)

    def test_handle_not_found(self):
        client_id = 654321
        client = ClientUpdateInput(
            name='Simon',
            last_name='Santander',
            rol='vice'
        )
        result = self.use_case.handle(client_id, client)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(result.message, ClientMessages.NOT_FOUND)


class DeleteClientTestCase(TestCase):

    def setUp(self):
        connect('mongoenginetest', host='mongomock://localhost')
        self.client_a = Client(
            identification = 123456789,
            identification_type = 'CC'
        )
        self.client_a.save()
        self.client_b = Client(
            identification = 765423,
            identification_type = 'CC'
        )
        self.client_b.save()
        self.user_a = User(
            username = self.client_a.identification,
            password = 'A1B2C3'
        )
        self.user_a.save()
        self.use_case = DeleteClient()

    def tearDown(self):
        disconnect()

    def test_handle_success(self):
        client_id = 123456789
        result = self.use_case.handle(client_id)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.message, ClientMessages.DELETED)

    def test_handle_client_not_found(self):
        client_id = 91827374
        result = self.use_case.handle(client_id)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(result.message, ClientMessages.NOT_FOUND)

    def test_handle_user_not_found(self):
        client_id = 765423
        result = self.use_case.handle(client_id)

        self.assertIsInstance(result, ClientResponse)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(result.message, UserMessages.NOT_FOUND)
