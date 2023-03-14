import re
import hashlib
import json

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

# crypte le mot de passe.
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# imprime le mode de passe.
def print_password(password):
    print(f"Valid password !\n"
          f"Password encrypt is : {encrypt_password(password)}")

# enregistre les mots de passe, les ajoute dans un fichier json et vérifie les doublons.
def manage_password(password):
    with open("passwords.json", "r") as f:
        list_password = json.load(f)
    if password not in list_password:
        print_password(password)
        list_password.append(password)
        with open("passwords.json", "w") as f:
            json.dump(list_password, f)
    else:
        print("Ce mot de passe existe déjà\n")
        menu_password()