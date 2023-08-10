from password_manager.rules import (
    LengthRule,
    ContainsLowercaseRule,
    ContainsUppercaseRule,
    ContainsDigitRule,
    ContainsSpecialRule,
)
from password_manager.website import Website


class LinkedinWebsite(Website):
    rules = [
        LengthRule(min_length=10, max_length=20),
        ContainsLowercaseRule(),
        ContainsUppercaseRule(),
        ContainsDigitRule(),
        ContainsSpecialRule(),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "linkedin.com" in url  # TODO urlparse

    @staticmethod
    def canonical_url() -> str:
        return "https://www.linkedin.com"
