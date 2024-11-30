import re


def validar_senha(senha):
    letras_min = 0
    letras_mai = 0
    numeros = 0
    simbolos = 0
    for termo in senha:
        if 'abcdefghijklmnopqrstuvwxyz'.find(termo) != -1:
            letras_min += 1
        elif 'abcdefghijklmnopqrstuvwxyz'.upper().find(termo) != -1:
            letras_mai += 1
        elif '1234567890'.find(termo) != -1:
            numeros += 1
        elif '!@#$%&*()_+=-[]{}.,/?\\\'\"'.find(termo) != -1:
            simbolos += 1
        else:
            return False
    if letras_mai + letras_min + numeros + simbolos < 8:
        return False
    return True
