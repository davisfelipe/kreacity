from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from src.utils import DateTime


def res_path(path: str):
    source = 'src.utils.date_and_time'
    return ".".join([source, path])


class DateTimeTestCase(TestCase):

    @patch(res_path('datetime'))
    def test_current_date(self, mock_date: Mock):
        date = datetime(2021, 2, 4, 19, 30)
        mock_date.utcnow.return_value = date

        current_datetime = DateTime.current_datetime()

        self.assertIsInstance(current_datetime, datetime)
        self.assertIsNotNone(current_datetime)
        self.assertEqual(date.year, current_datetime.year)

    @patch(res_path('datetime'))
    def test_expiration_date(self, mock_date: Mock):
        date = datetime(2021, 2, 4, 19, 30, 30)
        mock_date.utcnow.return_value = date

        delta_time = DateTime.expiration_date(minutes=5)

        self.assertIsInstance(delta_time, datetime)
        self.assertGreater(date.timestamp(), delta_time.timestamp())

    def test_from_timestamp(self):
        date = datetime(2021, 3, 15, 20, 4)
        timestamp_datetime = date.timestamp()

        current_date = DateTime.from_timestamp(timestamp_datetime)

        self.assertIsInstance(current_date, datetime)
        self.assertEqual(current_date.year, date.year)
        self.assertEqual(current_date.minute, date.minute)
