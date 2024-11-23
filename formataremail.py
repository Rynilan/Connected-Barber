def formatar_nome_email(email):
    if any(letra.isupper() for letra in email):
        raise ValueError("O e-mail não pode conter letras maiúsculas.")
    nome_usuario = email.split('@')[0]
    nome_formatado = '.'.join([parte.capitalize() for parte in nome_usuario.split('.')])
    dominio = email.split('@')[1]
    return f"{nome_formatado}@{dominio}"

email = ""
email_formatado = formatar_nome_email(email)
print(email_formatado)

email_invalid = ""
try:
    email_formatado_invalid = formatar_nome_email(email_invalid)
    print(email_formatado_invalid)
except ValueError as e:
    print(e)
