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
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# affiche le mode de passe hashé.
def print_password(password):
    print(f"Mot de passe valide !\n"
          f"Votre mot de passe crypté : {encrypt_password(password)}")

# sauvegarde les mots de passe hashés en veillant à ne pas ajouter les doublons dans le fichier json.
def save_password(password):
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

# affiche les mots de passe enregistrés.
def show_password():
    with open('passwords.json', 'r') as f:
        list_password = json.load(f)
    print(f"Voici les mots de passes enregistrés:\n{list_password}")

# permet à l'utilisateur de saisir son mot de passe et de le sauvegarder si valide.
def menu_password():
    while True:
        password = ask_password()
        if check_password(password):
            save_password(encrypt_password(password))
            break
        else:
            print("Mot de passe invalide.")

# définition du menu principale (main), affiche le menu et exécute les fonctions correspondantes en fonction de l'option choisie par l'utilisateur.
def main():
    while True:
        print(menu)
        print("Choisissez votre option : ")
        choice = input("> ")
        if choice == "1":
            print(exigences)
            menu_password()
        elif choice == "2":
            show_password()
        elif choice == "3":
            quit("À bientôt !")
        else:
            print("Choix invalide.")

# condition qui vérifie si le script est exécuté en tant que programme principal.
if __name__ == '__main__':
    main() # appel la fonction main() si le script est exécuté en tant que programme.