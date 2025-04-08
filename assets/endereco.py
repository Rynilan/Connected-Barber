class endereco:
    def __init__(self, pais, estado, cidade, rua, numero, cep, fuso_horario, complemento, barbearia):
        self.__barbearia = barbearia
        self.__pais = pais
        self.__estado = estado
        self.__cidade = cidade
        self.__cep = cep
        self.complemento = complemento

    def get_pais(self):
        return self.__pais

    def get_estado(self):
        return self.__estado

    def get_cidade(self):
        return self.__cidade

    def get_cep(self):
        return self.__cep

    def get_complemento(self):
        return self.__complemento

    def __verificar_permissao(self, operador):
        return (operador.comparar_barbearia(self.__barbearia) and operador.get_nivel() == 'adm')

    def set_pais(self: object, operador: object, pais: str) -> None:
        if self.__verificar_permissao(operador):
            self.__pais = pais

    def set_estado(self: object, operador: object, estado: str) -> None:
        if self.__verificar_permissao(operador):
            self.__estado = estado

    def set_cidade(self: object, operador: object, cidade: str) -> None:
        if self.__verificar_permissao(operador):
            self.__cidade = cidade

    def set_cep(self: object, operador: object, cep: str) -> None:
        if self.__verificar_permissao(operador):
            self.__cep = cep

    def set_complemento(self: object, operador: object, complemento: str) -> None:
        if self.__verificar_permissao(operador):
            self.__complemento = complemento
