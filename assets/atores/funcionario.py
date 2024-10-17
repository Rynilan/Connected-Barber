import Portfolio *
import Ator *

class Funcionario(Ator):
    def __init__(self, Nome, Data_de_nascimento, Senha, Telefone, E-mail, Fotos, Descricao):
        super().__init__(Nome, Data_de_nascimento, Senha, Telefone, E-mail)

    def Criarportfolio(self, Foto, Descricao):
        self.Portfolio = Portfolio(Fotos, Descricao)
    
    def Adicionarimagem(self, Fotos):
        self.Portfolio.Adicionar_imagem(Fotos)

    def Remover_imagem(Fotos):
        self.portfolio.Remover_imagem(Fotos)
    
    def Realizar_agendamento(Cliente, Servicos, Data_horario, Situacao):
        ...
        # em desenvolvimento(falta a conexão com o banco)

    def Cocluir_agendamento(cliente, servicos, Data_horario, Situacao)
        ...
        # em desenvolvimento(falta a conexão com o banco)

    def Adicionar_preferencia(Cliente, Preferencia):
        Cliente.Adicionar_preferencia(Preferencia)

