class portfolio:
    def __init__(self, fotos, descricao, dono):
        self.__dono = dono
        self.__fotos = fotos
        self.__descricao = descricao

    def get_imagens(self):
        return self.imagens

    def get_descricao(self):
        return self.descricao

    def __verificar_permissao(self, operador):
        return (self.__dono is operador or
                (self.__dono.comparar_barbearia(operador.get_barbearia()) and operador.get_nivel() == 'adm'))

    def set_descricao(self, operador, descricao):
        if self.__verificar_permissao(operador):
            self.__descricao = descricao

    def adicionar_foto(self, operador, foto):
        if self.__verificar_permissao(operador):
            self.__fotos = list(self.__fotos)
            self.__fotos.append(foto)
            self.__fotos = tuple(self.__fotos)

    def excluir_foto(self, operador, foto):
        if self.__verificar_permissao:
            self.__fotos = list(self.__fotos)
            self.__fotos.pop(self.__fotos.index(foto))
            self.__fotos = tuple(self.__fotos)
