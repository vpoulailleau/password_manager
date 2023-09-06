from password_manager.period import TrimestrialPeriod
from password_manager.rules import (
    LengthRule,
    ContainsDigitRule,
)
from password_manager.website import Website


class BanquePopulaireWebsite(Website):
    period = TrimestrialPeriod()
    rules = [
        LengthRule(min_length=8, max_length=8),
        ContainsDigitRule(),
    ]

    @classmethod
    def is_for(cls, url: str) -> bool:
        return "banquepopulaire.fr" in url

    @staticmethod
    def canonical_url() -> str:
        return "https://www.banquepopulaire.fr"
