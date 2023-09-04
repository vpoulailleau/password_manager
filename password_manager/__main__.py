from getpass import getpass

from password_manager.password import generate_passwords

if __name__ == "__main__":
    email = input("Entrez votre email : ")
    general_password = getpass("Entrez votre mot de passe principal : ")
    general_password_2 = getpass("Confirmez votre mot de passe principal : ")
    if general_password != general_password_2:
        print("Les mots de passe ne sont pas identiques")
    else:
        url = input("Entrez l'adresse du site pour lequel il faut un mot de passe : ")
        generate_passwords(email, general_password, url)
