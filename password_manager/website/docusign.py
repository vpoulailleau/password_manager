from password_manager.period import YearlyPeriod
from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
    NoMatchRule,
)
from password_manager.website import Website


class DocusignWebsite(Website):
    period = YearlyPeriod()
    rules = [
        LengthRule(min_length=6, max_length=20),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(),
        NoMatchRule(regex="[ <>]"),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "docusign." in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.docusign.com/"
