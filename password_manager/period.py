from datetime import date, timedelta


class Period:
    period_length = timedelta(days=7)

    def __init__(self, start: date | None = None) -> None:
        if start is None:
            self._start = date.today()
        else:
            self._start = start

    @property
    def start(self) -> date:
        return self._start

    def __str__(self) -> str:
        return self.start.strftime("%Y%m%d")

    def date_for_period(self, period: int) -> str:
        new_period = Period(start=self.start - abs(period) * self.period_length)
        return str(new_period)


class TrimestrialPeriod(Period):
    period_length = timedelta(days=31 * 3)

    @property
    def start(self) -> date:
        return date(year=self._start.year, month=self._start.month % 3 + 1, day=1)


class MonthlyPeriod(Period):
    period_length = timedelta(days=31)

    @property
    def start(self) -> date:
        return date(year=self._start.year, month=self._start.month, day=1)
