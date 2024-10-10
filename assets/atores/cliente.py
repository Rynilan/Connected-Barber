class Cliente:
    def __init__(self, nome, data_de_nascimento, senha, telefone, email, cep):
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__senha = senha
        self.__telefone = telefone
        self.__email = email
        self.__nivel = 'cliente'
        self.__cep = cep
        self.__preferencias = tuple()

    # Getters
    def get_nome(self, operador):
        if operador is self:
            return self.__nome

    def get_data_de_nascimento(self, operador):
        if operador is self:
            return self.__data_de_nascimento

    def get_senha(self, operador):
        if operador is self:
            return self.__senha

    def get_telefone(self, operador):
        if operador is self:
            return self.__telefone

    def get_email(self, operador):
        if operador is self:
            return self.__email

    def get_nivel(self, operador):
        if operador is self:
            return self.nivel

    def get_cep(self, operador):
        if operador is self:
            return self.__cep

    # Getters
    def set_nome(self, operador, nome):
        if operador is self:
            self.__nome = nome

    def set_data_de_nascimento(self, operador, data_de_nascimento):
        if operador is self:
            self.__data_de_nascimento = data_de_nascimento

    def set_senha(self, operador, senha):
        if operador is self:
            self.__senha = senha

    def set_telefone(self, operador, telefone):
        if operador is self:
            self.__telefone = telefone

    def set_email(self, operador, email):
        if operador is self:
            self.__email = email

    def set_cep(self, operador, cep):
        if operador is self:
            self.__cep = cep

    # Funcionário pegando informações diretamente do cliente.
    def __verificar_funcionario(self, operador):
        """ Observa se um dado funcionário está em algum dos agendamentos
            pendentes do cliente, se sim retorna True, senão, False. """
        if len(self.obter_agendamentos(self), (
            'funcionario="{}"'.format(operador.get_email(operador)),
            'situacao="pendente"'
        )):
            return True
        return False

    def get_preferencias(self, operador):
        if self.__verificar_funcionario(operador):
            return self.__preferencias

    def adicionar_preferencia(self, operador, preferencia):
        if self.__verificar_funcionario(operador):
            self.__preferencias = list(self.__preferencias)
            self.__preferencias.append(preferencia)
            self.__preferencias = tuple(self.__preferencias)

    # Cliente interagindo com agendamentos.
    def obter_agendamentos(self, filtro=None):
        # IMPOSSÍVEL IMPLEMENTAÇÃO NO MOMENTO, DEPENDE DA CONEXÃO COM O BANCO
        # DE DADOS. FEITO NO DIA: 10/10/2024
        ...

    def dar_feedback(self, agendamento, feedback):
        if agendamento.get_cliente(self) is self:
            agendamento.registrar_feedback(feedback)
