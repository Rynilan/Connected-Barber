from os import path
from abc import ABC, abstractmethod


class Oferecimento(ABC):
    def __init__(self: object,
                 nome: str,
                 descricao: str,
                 fotos: tuple[path],
                 valor: float) -> None:
        self._nome = nome
        self._descricao = descricao
        self._fotos = fotos
        self._valor = valor
        super().__init__()

    def get_fotos(self: object) -> tuple[path]:
        return self._fotos

    def get_descricao(self: object) -> str:
        return self._descricao

    def get_valor(self: object) -> float:
        return self._valor

    @abstractmethod
    def calcular_preco(self: object) -> int:
        pass
