import re

# demande le mot de passe.
def ask_password():
    password = input("Veuillez entrer votre mot de passe: ")
    return password

# vérifie la conformité du mot de passe.
def check_password():
    while True:
        password = input("Veuillez entrer votre mot de passe: ")
        if len(password) < 8:
            print("Veillez à ce que votre mot de passe contienne au moins 8 lettres.")
        elif not re.search(r"\d", password):
            print("Veillez à ce que votre mot de passe contienne un chiffre")
        elif not re.search(r"[A-Z]", password):
            print("Veillez à ce que votre mot de passe contienne une majuscule.")
        elif not re.search(r"[a-z]", password):
            print("Veillez à ce que votre mot de passe contienne une minuscule.")
        elif not re.search(r"[!@#$%^&*]", password):
            print("Veillez à ce que votre mot de passe contienne au moins un caractère spécial (!, @, #, $, %, ^, &, *)")
        else:
            print("Mot de passe valide")
            break

check_password()