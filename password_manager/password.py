
def generate_password(email: str, general_password: str, url: str) -> None:
    pass

def generate_passwords(email: str, general_password: str, url: str) -> None:
    # for last 3 periods
    general_password(email, general_password, url)


if __name__ == "__main__":
    email = input("Entrez votre email : ")
    general_password = input("Entrez votre mot de passe principal : ")
    url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")

    generate_passwords(email, general_password, url)
