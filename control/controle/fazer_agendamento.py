from model.tabela_agendamentos.CRUD import insert
from control.validadores.validacao_email import validar_email
from datetime import datetime


def fazer_agendamento(
    cliente: str,
    servico: int,
    funcionario: str,
    data: datetime,
) -> None:
    """ cliente e funcionário representam uma chave estrangeira, o email
        de cada um """
    if not (validar_email(cliente) or validar_email(funcionario)):
        ValueError('Email inválido')
    insert(cliente, servico, funcionario, data, 'marcado')
