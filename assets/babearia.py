from assets.endereco import Endereco
from assets.oferecimentos.servico import Servico


class Barbearia:
    def _init_(self, nome, pais, cidade, estado, rua, numero, cep, horario, funcionario_nome, servico_nome, servico_preco):
        self.__nome = nome[:50]  # Limitar a 50 caracteres
        self.__endereco = Endereco(
            pais,
            cidade,
            estado,
            rua,
            numero,
            cep
        )
        self.__horario = horario  # Deve ser uma tupla
        self.__funcionarios = None  # O primeiro funcionário deve ser definido pelo método adicionar_primeiro_funcionário logo após a criação da classe barbearia.
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

    # Adicionar novos serviços (somente administrador)
    def adicionar_servico(self, operador, servico):
        if operador.get_nivel() == 'adm':
            self.__servicos = list(self.__servicos)
            self.__servicos.append(servico)
            self.__servicos = tuple(self.__servicos)
        else:
            raise PermissionError("Somente o administrador pode adicionar serviços.")

    # Adicionar novos funcionários (somente administrador)
    def adicionar_funcionario(self, operador, funcionario):
        if operador.get_nivel() == 'adm':
            self.__funcionarios = list(self.__funcionarios)
            self.__funcionarios.append(funcionario)
            self.__funcionarios = tuple(self.__funcionarios)
        else:
            raise PermissionError("Somente o administrador pode adicionar funcionários.")

    # Adicionar produtos
    def adicionar_produto(self, operador, produto):
        if operador.get_nivel() == 'adm':
            self.__produtos = list(self.__produtos)
            self.__produtos.append(produto)
            self.__produtos = tuple(self.__produtos)
        else:
            raise PermissionError("Somente o administrador pode adicionar produtos.")

    # Adicionar ou atualizar portfólio
    def adicionar_portfolio(self, operador, portfolio):
        if operador.get_nivel() == 'adm':
            self.__portfolio = portfolio
        else:
            raise PermissionError("Somente o administrador pode atualizar o portfólio.")

    # Setter
    def setter(self, operador, atributo, valor):
        if operador.get_nivel() == 'adm':
            match atributo:
                case 'servico':
                    self.__servicos[self.__servicos.index(valor)] = valor
                case 'produto':
                    self.__produtos[self.__produtos.index(valor)] = valor
                case 'portfolio':
                    self.__portfolio = valor
                case 'funcionario':
                    self.__funcionarios[self.__funcionarios.index(valor)] = valor
                case _:
                    raise ValueError("atributo não encontrado")

    def excluir_funcionario(self, operador, funcionario):
        if operador.get_nivel() == 'adm':
            self.__funcionarios = list(self.__funcionarios)
            self.__funcionarios.pop(self.__funcionarios.index(funcionario))
            self.__funcionarios = tuple(self.__funcionarios)
    def excluir_produto(self, operador, produto):
        if operador.get_nivel() == 'adm':
            self.__produtos = list(self.__produtos)
            self.__produtos.pop(self.__produtos.index(produto))
            self.__produtos = tuple(self.__produtos)

    def excluir_servico(self, operador, servico):
        if operador.get_nivel() == 'adm':
            self.__servicos = list(self.__servicos)
            self.__servicos.pop(self.__servicos.index(servico))
            self.__servicos = tuple(self.__servicos)
    
    def excluir_tudo(self, operador):
        if operador.get_nivel() == 'adm':
            # Comando para excluir do banco de dados.
            self = None

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
