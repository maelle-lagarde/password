# gérer les mots de passe en enregistrant les mdp hachés dans un fichier.

import json

def manage_password(password):
    with open("passwords.json", "r") as f:
        list_password = json.load(f)
    if password not in list_password:
        print_password(password)
        list_password.append(password)
        with open("passwords.json", "w") as f:
            json.dump(list_password, f)
    else:
        print("Ce mot de passe exste déjà\n")
        menu_password()