from assets.oferecimentos.oferecimento import Oferecimento


class servicos(Oferecimento):

    def __init__(self, nome, descricao, fotos, valor, duracao):
        super().__init__(nome, descricao, fotos, valor)
        self.__duracao = duracao
        # Representa o tempo em minutos que o serviço demora a ser concluido.

    def get_duracao(self: object) -> int:
        return self.__duracao

    def set_duracao(self: object, operador: object, duracao: int) -> None:
        if super().comparar_barberia(operador.get_barbearia()):
            self.__duracao = duracao
