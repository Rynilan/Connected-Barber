class Barbearia:
    def _init_(self, nome, pais, cidade, estado, rua, numero, cep, horario, funcionario_nome, funcionario_cargo, servico_nome, servico_preco):
        self.__nome = nome[:50]  # Limitar a 50 caracteres
        self.__endereco = {
            'pais': pais,
            'cidade': cidade,
            'estado': estado,
            'rua': rua,
            'numero': numero,
            'cep': cep
        }
        self.__horario = horario  # Deve ser uma tupla 
        self.__funcionarios = [{'nome': funcionario_nome, 'cargo': funcionario_cargo}]  # Iniciando com o funcionário que cadastrou
        self.__servicos = [{'nome': servico_nome, 'preco': servico_preco}]  # Iniciando com o serviço
        self.__produtos = []
        self.__portfolio = None
        self.__administrador = {'nome': funcionario_nome, 'cargo': funcionario_cargo}  # Administrador é o funcionário que cadastrou

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
        return self._portfolio if self._portfolio else None

    # Adicionar novos serviços (somente administrador)
    def adicionar_servico(self, servico_nome, servico_preco, usuario_nome):
        if usuario_nome == self.__administrador['nome']:
            self.__servicos.append({'nome': servico_nome, 'preco': servico_preco})
        else:
            raise PermissionError("Somente o administrador pode adicionar serviços.")

    # Adicionar novos funcionários (somente administrador)
    def adicionar_funcionario(self, funcionario_nome, funcionario_cargo, usuario_nome):
        if usuario_nome == self.__administrador['nome']:
            self.__funcionarios.append({'nome': funcionario_nome, 'cargo': funcionario_cargo})
        else:
            raise PermissionError("Somente o administrador pode adicionar funcionários.")

    # Adicionar produtos
    def adicionar_produto(self, produto_nome, produto_preco, usuario_nome):
        if usuario_nome == self.__administrador['nome']:
            self.__produtos.append({'nome': produto_nome, 'preco': produto_preco})
        else:
            raise PermissionError("Somente o administrador pode adicionar produtos.")

    # Adicionar ou atualizar portfólio
    def adicionar_portfolio(self, portfolio_descricao, usuario_nome):
        if usuario_nome == self.__administrador['nome']:
            self.__portfolio = {'descricao': portfolio_descricao}
        else:
            raise PermissionError("Somente o administrador pode atualizar o portfólio.")

# Exemplo de uso
barbearia = Barbearia(
    nome="Barbearia Exemplo", 
    pais="Brasil", 
    cidade="São Paulo", 
    estado="SP", 
    rua="Rua Exemplo", 
    numero=123, 
    cep="12345-678", 
    horario=("09:00", "18:00"), 
    funcionario_nome="João", 
    funcionario_cargo="Gerente", 
    servico_nome="Corte de cabelo", 
    servico_preco=30.0
)

# Acessar os dados da barbearia
print(barbearia.get_nome())
print(barbearia.get_endereco())
print(barbearia.get_funcionarios())
print(barbearia.get_servicos())

# Adicionar novos serviços e funcionários
barbearia.adicionar_servico("Barba", 15.0, "João")
barbearia.adicionar_funcionario("Pedro", "Cabeleireiro", "João")

# Exibir serviços e funcionários atualizados
print(barbearia.get_servicos())
print(barbearia.get_funcionarios())

# Adicionar produtos e portfólio
barbearia.adicionar_produto("Pomada para cabelo", 20.0, "João")
barbearia.adicionar_portfolio("Portfólio de cortes de cabelo", "João")

# Exibir produtos e portfólio
print(barbearia.get_produtos())
print(barbearia.get_portfolio())