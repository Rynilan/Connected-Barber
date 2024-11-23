from model.tabela_agendamentos.CRUD import update


def cancelar_agendamento(id) -> None:
    update(id, ('situacao', ), ('cancelado', ))
