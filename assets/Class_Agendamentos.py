Classe agendamento:
class Agendamento:
    def _init_(self, cliente, funcionario, servico, data, situacao):
        self.__cliente = cliente  # Objeto do tipo Cliente
        self.__funcionario = funcionario  # Objeto do tipo Funcionario
        self.__servico = servico  # Objeto do tipo Servico
        self.__data = data  # Data do agendamento
        self.__situacao = situacao  # Situação inicial do agendamento (ex.: "Pendente", "Concluído", "Cancelado")

    # Getters
    def get_cliente(self):
        return self.__cliente

    def get_funcionario(self):
        return self.__funcionario

    def get_servico(self):
        return self.__servico

    def get_data(self):
        return self.__data

    def get_situacao(self):
        return self.__situacao

    # Setter exclusivo para alterar a situação do agendamento
    def set_situacao(self, nova_situacao):
        self.__situacao = nova_situacao

# Exemplo de como pode ser usado

class Cliente:
    def _init_(self, nome):
        self.nome = nome

    def obter_dados(self):
        return {'nome': self.nome}

# Exemplo básico para simular o uso com outros objetos

#cliente = Cliente("Carlos")
#funcionario = {'nome': "João", 'cargo': "Cabeleireiro"}  # Simulação de um objeto Funcionario
#servico = {'nome': "Corte de cabelo", 'preco': 30.0}  # Simulação de um objeto Servico
#data = "2024-10-10 15:00"  # Exemplo de data

# Criar um agendamento
#agendamento = Agendamento(cliente, funcionario, servico, data, "Pendente")

# Acessar dados do agendamento
#print(agendamento.get_cliente().obter_dados())
#print(agendamento.get_funcionario())
#print(agendamento.get_servico())
#print(agendamento.get_data())
#print(agendamento.get_situacao())

# Alterar a situação do agendamento
#agendamento.set_situacao("Concluído")
#print(agendamento.get_situacao())