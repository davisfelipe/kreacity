from datetime import datetime, timedelta
from typing import Union

from pytz import timezone


class DateTime:
    local_timezone = timezone('America/Bogota')

    @classmethod
    def current_datetime(cls) -> datetime:
        utc_timezone = timezone('UTC')
        now = datetime.utcnow()
        return now.replace(tzinfo=utc_timezone).astimezone(cls.local_timezone)

    @classmethod
    def expiration_date(cls, minutes: int = 0, hours: int = 0) -> datetime:
        return cls.current_datetime() + timedelta(minutes=minutes, hours=hours)

    @classmethod
    def from_timestamp(cls, time: Union[int, float]) -> datetime:
        return datetime.fromtimestamp(time, tz=cls.local_timezone)

