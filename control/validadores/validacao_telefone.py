def validar_telefone(telefone):
    if len(telefone) != 12:
        return False
    for termo in telefone:
        if termo not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            return False
    return True
