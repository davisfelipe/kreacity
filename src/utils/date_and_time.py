from datetime import datetime, timedelta

from pytz import timezone


class DateTime:

    @classmethod
    def current_datetime(cls) -> datetime:
        utc_timezone = timezone('UTC')
        local_timezone = timezone('America/Bogota')

        now = datetime.utcnow()
        return now.replace(tzinfo=utc_timezone).astimezone(local_timezone)

    @classmethod
    def expiration_date(cls, minutes: int = 0, hours: int = 0) -> datetime:
        return cls.current_datetime() + timedelta(minutes=minutes, hours=hours)

