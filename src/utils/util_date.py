import datetime

from datetime import timedelta


class DateUtils:
    @staticmethod
    def before_duration(duration):
        today = datetime.datetime.today()
        delta = timedelta(days=duration)
        past = today - delta
        year, month, day = past.year, past.month, past.day
        return f'{year}-{month}-{day}'
