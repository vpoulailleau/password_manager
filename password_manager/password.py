import hashlib

from password_manager.random import rand, srand
from password_manager.rules import CharacterSetRule, LengthRule
from password_manager.website.website import Website


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
    for period in range(3):
        print(period, "  =>  ", generate_password(email, general_password, url, period))


if __name__ == "__main__":
    # email = input("Entrez votre email : ")
    # general_password = input("Entrez votre mot de passe principal : ")
    # url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")
    email = "vpoulailleau@gmail.com"
    general_password = "password"  # nosec
    url = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fnotifications%2F%3Ffilter%3Dall&trk=login_reg_redirect"

    generate_passwords(email, general_password, url)
