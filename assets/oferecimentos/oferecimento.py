from os import path


class Oferecimento:
    def __init__(self: object,
                 nome: str,
                 descricao: str,
                 fotos: tuple[path],
                 valor: float,
                 barbearia: object) -> None:
        self._nome = nome
        self._descricao = descricao
        self._fotos = fotos
        self._valor = valor
        self._barbearia = barbearia

    def get_fotos(self: object) -> tuple[path]:
        return self._fotos

    def get_descricao(self: object) -> str:
        return self._descricao

    def get_valor(self: object) -> float:
        return self._valor

    def get_barbearia(self: object) -> object:
        return self._barbearia

    def set_valor(self: object, operador: object, valor: float) -> None:
        if operador.compare_barbearia(self._barbearia):
            self._valor = valor

    def set_descricao(self: object, operador: object, descricao: str) -> None:
        if operador.compare_barbearia(self._barbearia):
            self._descricao = descricao

    def adicionar_foto(self: object, operador: object, foto: str) -> None:
        if (operador.compare_barbearia(self._barbearia) and
                operador.get_nivel() == 'adm'):
            self._fotos = list(self._fotos)
            self._fotos.append(foto)
            self._fotos = tuple(self._fotos)

    def remover_foto(self: object, operador: object, foto: str) -> None:
        if (operador.compare_barbearia(self._barbearia) and
                operador.get_nivel() == 'adm'):
            self._fotos = list(self._fotos)
            self._fotos.pop(self._fotos.index(foto))
            self._foto = tuple(self._fotos)
