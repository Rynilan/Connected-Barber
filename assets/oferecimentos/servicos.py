from assets.oferecimentos.oferecimento import Oferecimento


class servicos(Oferecimento):

    def __init__(self, nome, descricao, fotos, valor):
        super().__init__(nome, descricao, fotos, valor)
