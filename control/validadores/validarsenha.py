import re

def validar_senha(senha):
    if len(senha) >= 8 and re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', senha):
        return True
    else:
        return False
validar_senha()
