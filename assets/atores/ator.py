from datetime import date, datetime


class Ator:
    def __init__(self: object,
                 nome: str,
                 data_de_nascimento: date,
                 senha: str,
                 telefone: str,
                 email: str,
                 nivel: str) -> None:
        self._nome = nome
        self._data_de_nascimento
        self._senha = senha
        self._telefone = telefone
        self._email = email
        self._nivel = nivel

    def get_nivel(self: object) -> str:
        return self._nivel

    def get_email(self: object) -> str:
        return self._email

    def get_data_de_nascimento(self: object) -> date:
        return self._data_de_nascimento

    def get_telefone(self: object) -> str:
        return self._telefone

    def get_nome(self: object) -> str:
        return self._nome

    def set_nome(self: object, operador: object, nome: str):
        if operador is self:
            self._nome = nome

    def set_data_de_nascimento(self: object,
                               operador: object,
                               data_de_nascimento: date):
        if operador is self:
            self._data_de_nascimento = data_de_nascimento

    def set_email(self: object, operador: object, email: str) -> None:
        if operador is self:
            self._email = email

    def set_senha(self: object, operador: object, senha: str) -> None:
        if operador is self:
            self._senha = senha

    def set_telefone(self: object, operador: object, telefone: str) -> None:
        if operador is self: 
            self._telefone = telefone

    def obter_meus_agendamentos(
            self: object,
            operador: object,
            intervalo: tuple[date, date]) -> tuple[str]:
        if operador is self:
            agendamentos = tuple()
            # Comando para retornar os registros de agendamentos references a
            # esse usuário dentro do intervalo especificado.
            return agendamentos

    def fazer_agendamento(self, cliente: object, funcionario: object,
                          horario: datetime, servico: object) -> None:
        ...
        # Comando para guardar essas informações sobre o agendamento
        # no banco de dados.

    def cancelar_agendamento(self: object, operador: object,
                             agendamento: object) -> None:
        agendamento.cancelar(operador)

    def atualizar_agendamento(self: object):
        # NÃO SEI COMO IMPLEMENTAR AINDA.
        ...
