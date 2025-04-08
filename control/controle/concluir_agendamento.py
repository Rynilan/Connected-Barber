from model.tabela_agendamentos.CRUD import update


def concluir_agendamento(ide):
    update(ide, ("status", ), ("conluido", ))
