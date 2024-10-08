from datetime import date


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
