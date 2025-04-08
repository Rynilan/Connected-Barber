class Barbearia:
    def _init_(self, nome, endereco, horario):
        self.__nome = nome[:50]  # Limitar a 50 caracteres
        self.__endereco = endereco
        self.__horario = horario
        # O primeiro funcionário deve ser definido pelo
        # método adicionar_funcionario logo após
        # a criação da classe barbearia.
        self.__funcionarios = tuple()
        self.__servicos = tuple()
        self.__produtos = tuple()
        self.__portfolio = None

    # Getters
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_horario(self):
        return self.__horario

    def get_funcionarios(self):
        return self.__funcionarios

    def get_servicos(self):
        return self.__servicos

    def get_produtos(self):
        return self.__produtos

    def get_portfolio(self):
        return self._portfolio

    def __verificar_permissao(self: object, operador: object) -> bool:
        """ Retorna 'True' se o operador tem ligação com a barbearia e é de
            nível administrador, senão retorna 'False'."""
        return (operador.get_nivel() == 'adm' and operador.comparar_barbearia(self))

    # Adicionar novos serviços (somente administrador)
    def adicionar_servico(self, operador, servico):
        if self.__verificar_permissao(operador):
            self.__servicos = list(self.__servicos)
            self.__servicos.append(servico)
            self.__servicos = tuple(self.__servicos)
        else:
            raise PermissionError("Somente o administrador pode adicionar serviços.")

    # Adicionar novos funcionários (somente administrador)
    def adicionar_funcionario(self, operador, funcionario):
        if self.__verificar_permissao(operador):
            self.__funcionarios = list(self.__funcionarios)
            self.__funcionarios.append(funcionario)
            self.__funcionarios = tuple(self.__funcionarios)
        else:
            raise PermissionError("Somente o administrador pode adicionar funcionários.")

    # Adicionar produtos
    def adicionar_produto(self, operador, produto):
        if self.__verificar_permissao(operador):
            self.__produtos = list(self.__produtos)
            self.__produtos.append(produto)
            self.__produtos = tuple(self.__produtos)
        else:
            raise PermissionError("Somente o administrador pode adicionar produtos.")

    # Adicionar ou atualizar portfólio
    def adicionar_portfolio(self, operador, portfolio):
        if self.__verificar_permissao(operador):
            self.__portfolio = portfolio
        else:
            raise PermissionError("Somente o administrador pode atualizar o portfólio.")

    # Setter
    def setter(self, operador, atributo, valor):
        if self.__verificar_permissao(operador):
            match atributo:
                case 'portfolio':
                    self.__portfolio = valor
                case 'endereco':
                    self.__endereco = valor
                case 'horario':
                    self.__horario = valor
                case _:
                    raise ValueError("atributo não encontrado")

    # Métodos de exclusão de ser.
    def excluir_funcionario(self, operador, funcionario):
        if self.__verificar_permissao(operador):
            self.__funcionarios = list(self.__funcionarios)
            self.__funcionarios.pop(self.__funcionarios.index(funcionario))
            self.__funcionarios = tuple(self.__funcionarios)

    def excluir_produto(self, operador, produto):
        if self.__verificar_permissao(operador):
            self.__produtos = list(self.__produtos)
            self.__produtos.pop(self.__produtos.index(produto))
            self.__produtos = tuple(self.__produtos)

    def excluir_servico(self, operador, servico):
        if self.__verificar_permissao(operador):
            self.__servicos = list(self.__servicos)
            self.__servicos.pop(self.__servicos.index(servico))
            self.__servicos = tuple(self.__servicos)

    def exclusao(self, operador):
        if self.__verificar_permissao(operador):
            # Comando para excluir do banco de dados.
            self = None

    # Métodos de edição de ser
    def editar_produto(self, operador, produto, produto_editado):
        if self.__verificar_permissao(operador):
            self.__produtos[self.__produtos.index(produto)] = produto_editado

    def editar_endereco(self, operador, endereco_editado):
        if self.__verificar_permissao(operador):
            self.__endereco = endereco_editado

    def editar_funcionario(self, operador, funcionario, funcionario_editado):
        if self.__verificar_permissao(operador):
            self.__funcionarios[self.__funcionarios.index(funcionario)] = funcionario_editado

    def editar_horario(self, operador, horario):
        if self.__verificar_permissao(operador):
            self.__horario = horario

    def editar_servico(self, operador, servico, servico_editado):
        if self.__verificar_permissao(operador):
            self.__servicos[self.__servicos.index(servico)] = servico_editado

    def editar_portfolio(self, operador, portfolio):
        self.adicionar_portfolio(operador, portfolio)

# Exemplo de uso
#barbearia = Barbearia(
    #nome="Barbearia Exemplo", 
    #pais="Brasil", 
    #cidade="São Paulo", 
    #estado="SP", 
    #rua="Rua Exemplo", 
    #numero=123, 
    #cep="12345-678", 
    #horario=("09:00", "18:00"), 
    #funcionario_nome="João", 
    #funcionario_cargo="Gerente", 
    #servico_nome="Corte de cabelo", 
    #servico_preco=30.0
#)

# Acessar os dados da barbearia
#print(barbearia.get_nome())
#print(barbearia.get_endereco())
#print(barbearia.get_funcionarios())
#print(barbearia.get_servicos())

# Adicionar novos serviços e funcionários
#barbearia.adicionar_servico("Barba", 15.0, "João")
#barbearia.adicionar_funcionario("Pedro", "Cabeleireiro", "João")

# Exibir serviços e funcionários atualizados
#print(barbearia.get_servicos())
#print(barbearia.get_funcionarios())

# Adicionar produtos e portfólio
#barbearia.adicionar_produto("Pomada para cabelo", 20.0, "João")
#barbearia.adicionar_portfolio("Portfólio de cortes de cabelo", "João")

# Exibir produtos e portfólio
#print(barbearia.get_produtos())
#print(barbearia.get_portfolio())
