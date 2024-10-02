from datetime import date
from abc import ABC, abstractmethod


class Ator(ABC):
    def __init__(self: object,
                 nome: str,
                 data_de_nascimento: date,
                 senha: str,
                 telefone: str,
                 email: str) -> None:
        self._nome = nome
        self._data_de_nascimento
        self.__senha = senha
        self._telefone = telefone
        self._email = email
        super().__init__()

    def get_email(self: object) -> str:
        return self._email

    def get_data_de_nascimento(self: object) -> date:
        return self._data_de_nascimento

    def get_telefone(self: object) -> str:
        return self._telefone

    def get_nome(self: object) -> str:
        return self._nome

    @abstractmethod
    def comparar_senha(self: object) -> int:
        pass
