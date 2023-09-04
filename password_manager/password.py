import hashlib
from contextlib import suppress

from password_manager.random import rand, srand
from password_manager.rules import CharacterSetRule, LengthRule, RuleError
from password_manager.website.website import Website


def _generate_password(website: type[Website]) -> str:
    password = ""  # nosec
    for rule in website.rules:
        if isinstance(rule, CharacterSetRule):
            password += rule.character_set[rand() % len(rule.character_set)]

    length = 10  # default length
    for rule in website.rules:
        if isinstance(rule, LengthRule):
            length = rule.max_length

    while len(password) < length:
        password += website.character_set()[rand() % len(website.character_set())]

    for rule in website.rules:
        if not rule.is_valid(password):
            raise RuleError
    return password


def generate_password(
    email: str, general_password: str, url: str, period: int = 0
) -> str:
    website = Website.website_for(url)
    if website is None:
        print("No website configuration found")
        return ""
    seed_str = (
        email
        + website.canonical_url()
        + general_password
        + website.period.date_for_period(period)
    )
    seed = int(hashlib.sha256(seed_str.encode(encoding="utf-8")).hexdigest(), 16)
    srand(seed)

    # try, stop at first correct generation
    for _ in range(100):
        with suppress(RuleError):
            return _generate_password(website)
    return "No password generation is possible"


def generate_passwords(email: str, general_password: str, url: str) -> None:
    website = Website.website_for(url)
    if website is None:
        print("No website configuration found")
        return
    print("Password for", website.canonical_url())
    for period in range(3):
        date = website.period.date_for_period(period)
        date = f"{date[0:4]}/{date[4:6]}/{date[6:8]}"
        print(
            "Since",
            date,
            "  =>  ",
            generate_password(email, general_password, url, period),
        )
