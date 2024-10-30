from model.tabela_agendamentos.CRUD import insert
from datetime import datetime


def fazer_agendamento(
    cliente: str,
    servico: int,
    funcionario: str,
    data: datetime,
) -> None:
    """ Cada um desses parâmetros representa uma chave estrangeira. """

    insert(cliente, servico, funcionario, data, 'marcado')
