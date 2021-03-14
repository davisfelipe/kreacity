from datetime import datetime

from pytz import timezone


class DateTime:

    @staticmethod
    def current_datetime() -> datetime:
        utc_timezone = timezone('UTC')
        local_timezone = timezone('America/Bogota')

        now = datetime.utcnow()
        return now.replace(tzinfo=utc_timezone).astimezone(local_timezone)
