from password_manager.period import YearlyPeriod
from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
)
from password_manager.website import Website


class MaprimerenovWebsite(Website):
    period = YearlyPeriod()
    rules = [
        LengthRule(min_length=8, max_length=20),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(character_set="!@#$%&*()-=+[];:,./?"),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "www.maprimerenov.gouv.fr" in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.maprimerenov.gouv.fr/"
