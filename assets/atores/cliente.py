from assets.atores.ator import Ator


class Cliente (Ator):
    def __init__(self, nome, data_de_nascimento, senha, telefone, email, cep):
        # Valida o CEP para garantir que ele tenha exatamente 11 caracteres
        super().__init__(nome, data_de_nascimento, senha, telefone, email, 'cliente')
        if len(cep) != 11:
            raise ValueError("O CEP deve ter exatamente 11 caracteres.")
        self.__cep = cep  # Armazena o CEP
        self.__preferencias = tuple()  # Armazena as preferências como tupla

    def get_cep(self, operador):
        if operador is self:
            return self.__cep

    def get_preferencias(self, operador):
        if operador.get_nivel() != 'clietne':
            return self.__preferencias

    def adicionar_preferencia(self, operador, preferencia):
        if operador.get_nivel() != 'cliente':
            self.__preferencias = list(self.__preferencias)
            self.__preferencias.append(preferencia)
            self.__preferencias = tuple(self.__preferencias)

    def dar_feedback(self, agendamento, feedback):
        if agendamento.get_cliente(self) is self:
            agendamento.registrar_feedback(feedback)
