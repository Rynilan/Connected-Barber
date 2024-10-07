from os import path


class Oferecimento:
    def __init__(self: object,
                 nome: str,
                 descricao: str,
                 fotos: tuple[path],
                 valor: float) -> None:
        self._nome = nome
        self._descricao = descricao
        self._fotos = fotos
        self._valor = valor

    def get_fotos(self: object) -> tuple[path]:
        return self._fotos

    def get_descricao(self: object) -> str:
        return self._descricao

    def get_valor(self: object) -> float:
        return self._valor

    def calcular_preco(self: object) -> int:
        pass
