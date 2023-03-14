# crypte les mots de passe.

import hashlib

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def print_password(password):
    print(f"Valid password !\n"
          f"Password encrypt is : {encrypt_password(password)}")