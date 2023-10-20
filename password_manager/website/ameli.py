from password_manager.period import YearlyPeriod
from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
)
from password_manager.website import Website


class AmeliWebsite(Website):
    period = YearlyPeriod()
    rules = [
        LengthRule(min_length=8, max_length=50),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(character_set="?!$£€@&(-+_)=*%/<>,.;:"),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "ameli.fr" in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.ameli.fr/"
