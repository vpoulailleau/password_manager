from password_manager.period import YearlyPeriod
from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
)
from password_manager.website import Website


class CalitomWebsite(Website):
    period = YearlyPeriod()
    rules = [
        LengthRule(min_length=6, max_length=32),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(character_set="-_."),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "calitom.com" in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.calitom.com/"
