import hashlib
import string
from datetime import date

from password_manager.random import rand, srand

CHARACTER_SET_LOWERCASE = string.ascii_lowercase
CHARACTER_SET_UPPERCASE = string.ascii_uppercase
CHARACTER_SET_DIGIT = string.digits
CHARACTER_SET_SPECIAL = "@#$<>()[]+-/*=%"


class Rule:
    def is_valid(self, password: str) -> bool:
        return False


class LengthRule(Rule):
    def __init__(self, min_length: int, max_length: int) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, password: str) -> bool:
        return self.min_length <= len(password) <= self.max_length


class CharacterSetRule(Rule):
    character_set: str = ""

    def is_valid(self, password: str) -> bool:
        return any(c in password for c in self.character_set)


class ContainsLowercaseRule(CharacterSetRule):
    character_set = CHARACTER_SET_LOWERCASE


class ContainsUppercaseRule(CharacterSetRule):
    character_set = CHARACTER_SET_UPPERCASE


class ContainsDigitRule(CharacterSetRule):
    character_set = CHARACTER_SET_DIGIT


class ContainsSpecialRule(CharacterSetRule):
    character_set = CHARACTER_SET_SPECIAL


class Website:
    all_websites: list[type["Website"]] = []
    rules: list[Rule] = []
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
    def date_for_period(period) -> str:
        raise NotImplementedError


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

    @staticmethod
    def date_for_period(period) -> str:
        return date.today().strftime("%Y%m01")  # monthly


def website_for(url: str) -> type[Website] | None:
    for website in Website.all_websites:
        if website.is_for(url):
            return website
    return None


def generate_password(email: str, general_password: str, url: str) -> str:
    website = website_for(url)
    if website is None:
        print("No website configuration found")
        return ""
    seed_str = (
        email + website.canonical_url() + general_password + website.date_for_period(0)
    )
    seed = int(hashlib.sha256(seed_str.encode(encoding="utf-8")).hexdigest(), 16)
    srand(seed)

    password = ""  # nosec
    for rule in website.rules:
        if isinstance(rule, CharacterSetRule):
            password += rule.character_set[rand() % len(rule.character_set)]

    length = 10
    for rule in website.rules:
        if isinstance(rule, LengthRule):
            length = rule.max_length

    while len(password) < length:
        password += website.character_set()[rand() % len(website.character_set())]

    # TODO assert all rules OK
    return password


def generate_passwords(email: str, general_password: str, url: str) -> None:
    # for last 3 periods
    print(generate_password(email, general_password, url))


if __name__ == "__main__":
    # email = input("Entrez votre email : ")
    # general_password = input("Entrez votre mot de passe principal : ")
    # url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")
    email = "vpoulailleau@gmail.com"
    general_password = "password"  # nosec
    url = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fnotifications%2F%3Ffilter%3Dall&trk=login_reg_redirect"

    generate_passwords(email, general_password, url)
