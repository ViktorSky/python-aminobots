from typing import Optional
from datetime import datetime
from dateutil.relativedelta import relativedelta

__all__ = ("Seconds",)


class Seconds:
    def __new__(cls,
                minutes: Optional[int] = 0,
                hours: Optional[int] = 0,
                days: Optional[int] = 0,
                weeks: Optional[int] = 0,
                months: Optional[int] = 0,
                years: Optional[int] = 0) -> int:
        date = datetime.now()
        custom = relativedelta(minutes=minutes, hours=hours, days=days, weeks=weeks, months=months, years=years)
        return int((date + custom).total_seconds())
