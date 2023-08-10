from datetime import date


class Website:
    all_websites: list[type["Website"]] = []

    def __init__(self) -> None:
        pass

    def __init_subclass__(cls) -> None:
        Website.all_websites.append(cls)

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


def generate_password(email: str, general_password: str, url: str) -> None:
    website = website_for(url)
    if website is None:
        print("No website configuration found")
        return
    seed = (
        email + website.canonical_url() + general_password + website.date_for_period(0)
    )
    print(seed)


def generate_passwords(email: str, general_password: str, url: str) -> None:
    # for last 3 periods
    generate_password(email, general_password, url)


if __name__ == "__main__":
    # email = input("Entrez votre email : ")
    # general_password = input("Entrez votre mot de passe principal : ")
    # url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")
    email = "vpoulailleau@gmail.com"
    general_password = "password"  # nosec
    url = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fnotifications%2F%3Ffilter%3Dall&trk=login_reg_redirect"

    generate_passwords(email, general_password, url)
