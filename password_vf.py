import re
import hashlib
import json

menu = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Ajouter votre mot de passe
2. Afficher les mots de passe enregistrés
3. Quitter
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

exigences = """
Voici les exigences de sécurité à respecter pour le mot de passe :
● Il doit contenir au moins 8 caractères.
● Il doit contenir au moins une lettre majuscule.
● Il doit contenir au moins une lettre minuscule.
● Il doit contenir au moins un chiffre.
● Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
"""

# demande le mot de passe et vérifie la conformité du mot de passe.
def add_password():
    while True:
        password = input("Veuillez entrer votre mot de passe: ")
        if len(password) < 8:
            print("Veuillez à ce que votre mot de passe contienne au moins 8 lettres.")
        elif not re.search(r"\d", password):
            print("Veuillez à ce que votre mot de passe contienne un chiffre")
        elif not re.search(r"[A-Z]", password):
            print("Veuillez à ce que votre mot de passe contienne une majuscule.")
        elif not re.search(r"[a-z]", password):
            print("Veuillez à ce que votre mot de passe contienne une minuscule.")
        elif not re.search(r"[!@#$%^&*]", password):
            print("Veuillez à ce que votre mot de passe contienne au moins un caractère spécial (!, @, #, $, %, ^, &, *)")
        else:
            print("Mot de passe valide.")
            break
    return True

# crypte le mot de passe.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# sauvegarde les mots de passe hashés en veillant à ne pas ajouter les doublons dans le fichier json.
def save_passwords(password):
    with open("passwords.json", "r") as f:
        list_passwords = json.load(f)
    hashed_passwords = hash_password(password)
    if hashed_passwords not in list_passwords:
        list_passwords.append(hashed_passwords)
        with open("passwords.json", "w") as f:
            json.dump(list_passwords, f)
        print("Le mot de passe a été ajouté avec succès")
    else:
        print("Le mot de passe existe déjà")

# affiche les mots de passe hashés et enregistrés.
def show_passwords(password):
    with open("passwords.json", "r") as f:
        list_passwords = json.load(f)
    if list_passwords:
        for password in list_passwords:
            print(password)
    else:
        print("Il n'y a pas de mots de passe enregistrés.")

# vérifie la conformité du mot de passe et enregistre le mot de passe chiffré.
def check_password(password):
    if add_password() == True:
        save_passwords(password)
        print("Mot de passe valide, bye bye!")
    else:
        print("Le mot de passe n'est pas valide, recommencez")
        add_password()

# affiche le menu principal.
def main():
    password = ""
    while True:
        print(menu)
        print("Choisissez votre option : ")
        choice = input("> ")
        if choice == "1":
            print(exigences)
            check_password(password)
        elif choice == "2":
            show_passwords(password)
        elif choice == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide.")

if __name__ == '__main__':
    main()