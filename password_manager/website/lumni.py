from password_manager.period import YearlyPeriod
from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
)
from password_manager.website import Website


class LumniWebsite(Website):
    period = YearlyPeriod()
    rules = [
        LengthRule(min_length=8, max_length=30),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "lumni.fr" in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.lumni.fr/"
