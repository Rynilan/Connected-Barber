from assets.oferecimentos.oferecimento import Oferecimento
from datetime import date


class produto(Oferecimento):
    def __init__(self, nome, descricao, foto, preco, marca, data_de_validade):
        super().__init__(nome, descricao, foto, preco)
        self.__marca = marca
        self.__data_de_validade = data_de_validade

    def get_marca(self: object) -> str:
        return self.__marca

    def get_data_de_validade(self: object) -> date:
        return self.__data_de_validade

    def set_data_de_validade(self: object, barbearia: object,
                             data_de_valiade: date) -> None:
        if super().comparar_barberia(barbearia):
            self.__data_de_validade = data_de_valiade

    def set_marca(self: object, barbearia: object, marca: str) -> None:
        if super().comparar_barberia(barbearia):
            self.__marca = marca
