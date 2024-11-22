import update from model.tabela_agendamentos.CRUD
def conc(ide):
    update(ide, ("status", ), ("conluido", ))
