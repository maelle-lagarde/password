# vérifie la conformité du mot de passe.

import string

letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
punctuation = "!@#$%^&*"

def check_password():
    while True:
        password = input("Veuillez entrer votre mot de passe: ")
        if len(password) < 8:
            print("Veillez à ce que votre mot de passe contienne au moins 8 lettres.")
        elif not any(char.isdigit() for char in password):
            print("Veillez à ce que votre mot de passe contienne un chiffre.")
        elif not any(char in letters_upper for char in password):
            print("Veillez à ce que votre mot de passe contienne une majuscule.")
        elif not any(char in letters_lower for char in password):
            print("Veillez à ce que votre mot de passe contienne une minuscule.")
        elif not any(char in punctuation for char in password):
            print("Veillez à ce que votre mot de passe contienne au moins un caractère spécial (!@#$%^&*)")
        else:
            print("Mot de passe valide !")
            break

check_password()

