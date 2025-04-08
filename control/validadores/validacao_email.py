from smtplib import SMTP
from random import random
from email.message import EmailMessage


def validar_email(email: str) -> bool:
    valido = True
    simbolo = False
    for letra in email[0:email.find('@')]:
        if letra not in (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ):
            valido = False
        elif letra not in ('.', '-', '_'):
            valido = False
            if simbolo is True:
                return False
            else:
                simbolo = True
        else:
            simbolo = False
    valido = not bool(
        email.startswith('.') or
        email.startswith('-') or
        email.startswith('_')
    )
    return valido


def enviar_email_de_validacao(email: str) -> None:
    """ Função que objetiva enviar um email de confirmação para confirmar
        o email. Ainda não funcional e falta ser implementada. """
    mensagem = EmailMessage()
    codigo = random() * 1000
    mensagem.set_content(
        'Código de validação de email: {:.0f}'.format(codigo) +
        'Não compartilhe esse código com ninguém.'
    )
    mensagem['Subject'] = 'Código de Verificação'
    mensagem['From'] = 'Equipe da Connected Barber'
    mensagem['To'] = email[email.find('@'):]
    conexao = SMTP('localhost')
    conexao.send_message(mensagem)
    conexao.quit()
    return codigo

