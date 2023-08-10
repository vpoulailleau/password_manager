from password_manager.password import generate_passwords

if __name__ == "__main__":
    # email = input("Entrez votre email : ")
    # general_password = input("Entrez votre mot de passe principal : ")
    # url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")
    email = "vpoulailleau@gmail.com"
    general_password = "password"  # nosec
    url = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fnotifications%2F%3Ffilter%3Dall&trk=login_reg_redirect"

    generate_passwords(email, general_password, url)
