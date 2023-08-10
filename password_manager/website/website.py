from password_manager.period import Period, TrimestrialPeriod
from password_manager.rules import Rule, CharacterSetRule


class Website:
    all_websites: list[type["Website"]] = []
    rules: list[Rule] = []
    period: Period = TrimestrialPeriod()
    _character_set: str = ""

    def __init_subclass__(cls) -> None:
        Website.all_websites.append(cls)

    @classmethod
    def character_set(cls) -> str:
        if not cls._character_set:
            for rule in cls.rules:
                if isinstance(rule, CharacterSetRule):
                    cls._character_set += rule.character_set
        return cls._character_set

    @classmethod
    def is_for(cls, url: str) -> bool:
        return False

    @staticmethod
    def canonical_url() -> str:
        raise NotImplementedError

    @staticmethod
    def website_for(url: str) -> type["Website"] | None:
        for website in Website.all_websites:
            if website.is_for(url):
                return website
        return None
