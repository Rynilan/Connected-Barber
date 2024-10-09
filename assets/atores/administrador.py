class Administrador:
    def __init__(self, barbearia, funcionario_pai):
        self.__barbearia = barbearia

    # Métodos de adição de ser.
    def adicionar_funcionario(self, funcionario):
        self.__barbearia.adicionar_funcionario(self, funcionario)

    def adicionar_servico(self, servico):
        self.__barbearia.adicionar_servico(self, servico)

    def adicionar_produto(self, produto):
        self.__barbearia.adicionar_produto(self, produto)

    def criar_portfolio(self, portfolio):
        self.__barbearia.adicionar_portfolio(self, portfolio)

    # Métodos de edição de ser.
    def editar_funcionario(self, funcionario):
        self.__barbearia.setter(self, 'funcionario', funcionario)

    def editar_servico(self, servico):
        self.__barbearia.setter(self, 'servico', servico)

    def editar_produto(self, produto):
        self.__barbearia.setter(self, 'produto', produto)

    def editar_portfolio(self, portfolio):
        self.criar_portfolio(portfolio)

    # Getters dos atributos da barbearia.
    def get_portifolio(self):
        return self.__barbearia.get_portfolio()

    def get_funcionarios(self):
        return self.__barbearia.get_funcionarios()

    def get_produtos(self):
        return self.__barbearia.get_produtos()

    def get_servicos(self):
        return self.__barbearia.get_servicos()

    # exclui o ser
    def excluir_funcionario(self, funcionario):
        self.__barbearia.excluir_funcionario(self, funcionario)

    def excluir_produto(self, produto):
        self.__barbearia.excluir_produto(self, produto)

    def excluir_portfolio(self, portfolio):
        self.__barbearia.setter(self, 'portfolio', None)

    def excluir_servico(self, servico):
        self.__barbearia.excluir_servico(self, servico)

    # Exclusão total da barbearia.
    def excluir_tudo(self):
        self.__barbearia.exclusao(self)

    def Aumenta_nivel(self, funcionario):
        funcionario.aumentar_nivel(self)

    def Baixar_nivel(self, funcionario):
        funcionario.baixar_nivel(self)
