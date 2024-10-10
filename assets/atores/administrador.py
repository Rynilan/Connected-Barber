class Administrador:
    def __init__(self, funcionario_pai):
        self.__pai = funcionario_pai

    # Métodos de adição de ser.
    def adicionar_funcionario(self, funcionario):
        self.get_barbearia().adicionar_funcionario(self, funcionario)

    def adicionar_servico(self, servico):
        self.get_barbearia().adicionar_servico(self, servico)

    def adicionar_produto(self, produto):
        self.get_barbearia().adicionar_produto(self, produto)

    def criar_portfolio(self, portfolio):
        self.get_barbearia().adicionar_portfolio(self, portfolio)

    # Métodos de edição de ser.
    def editar_funcionario(self, funcionario, funcionario_editado):
        self.get_barbearia().editar_funcionario(self, funcionario, funcionario_editado)

    def editar_servico(self, servico, servico_editado):
        self.get_barbearia().editar_servico(self, servico, servico_editado)

    def editar_produto(self, produto, produto_editado):
        self.get_barbearia().editar_produto(self, produto, produto_editado)

    def editar_portfolio(self, portfolio):
        self.criar_portfolio(portfolio)

    def editar_endereco(self, endereco):
        self.get_barbearia().editar_endereco(self, endereco)

    def editar_horario(self, horario):
        self.get_barbearia().editar_horario(self, horario)

    def editar_nome(self, nome):
        self.get_barbearia().editar_horario(self, nome)

    # exclui o ser
    def excluir_funcionario(self, funcionario):
        self.get_barbearia().excluir_funcionario(self, funcionario)

    def excluir_produto(self, produto):
        self.get_barbearia().excluir_produto(self, produto)

    def excluir_portfolio(self, portfolio):
        self.get_barbearia().setter(self, 'portfolio', None)

    def excluir_servico(self, servico):
        self.get_barbearia().excluir_servico(self, servico)

    # Exclusão total da barbearia.
    def excluisao(self):
        self.get_barbearia().exclusao(self)

    def Aumenta_nivel(self, funcionario):
        funcionario.aumentar_nivel(self)

    def Baixar_nivel(self, funcionario):
        funcionario.baixar_nivel(self)
