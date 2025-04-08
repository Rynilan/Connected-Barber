#Obs: Não esquecer de alterar o Nome do banco de dados na hora do uso  

class Admin():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

        # Método para atualizar atributos de um Admin
    def Atualiza_atributo(self, atributo, valor):
        if hasattr(self, atributo):
            setattr(self, atributo, valor)
            return getattr(self, atributo)
        else:
            return f"O atributo '{atributo}' não existe."

    # Método para adicionar informações (portfolio, funcionário, produto, serviço)
    def Adiciona_ser(self, portfolio, funcionario, produto, servico):
        self.portfolio = portfolio
        self.funcionario = funcionario
        self.produto = produto
        self.servico = servico

    # Métodos para obter e definir valores de cada atributo
    def get_portfolio(self):
        return self.portfolio

    def set_portfolio(self, portfolio):
        self.portfolio = portfolio

    def get_funcionario(self):
        return self.funcionario

    def set_funcionario(self, funcionario):
        self.funcionario = funcionario

    def get_produto(self):
        return self.produto

    def set_produto(self, produto):
        self.produto = produto

    def get_servico(self):
        return self.servico

    def set_servico(self, servico):
        self.servico = servico

    # Método para excluir o banco de dados
    @staticmethod
    def Excluir_tudo():
        try:
            # Conectar ao servidor MySQL
            conexao = mysql.connector.connect(
                host='localhost',        
                user='root',      
                password=''     
            )

            if conexao.is_connected():
                cursor = conexao.cursor()

                # Comando SQL para apagar o banco de dados
                sql = "DROP DATABASE IF EXISTS senac"
                
                # Executar o comando
                cursor.execute(sql)
                print("Banco de dados 'senac' apagado com sucesso!")

        except Error as erro:
            print(f"Erro ao apagar o banco de dados: {erro}")

        finally:
            # Fechar a conexão com o banco de dados ao final da tarefa
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    # Método para aumentar o nível de um funcionário
    def Aumenta_nivel(self, funcionario):
        funcionario.set_nivel("Adm")

    # Método para baixar o nível de um funcionário
    def Baixar_nivel(self, funcionario):
        funcionario.set_nivel("Funcionario")

    # Método para remover uma entrada do banco de dados
    @staticmethod
    def remover_entrada(funcionario, portfolio, produto, servico):
        try:
            # Conectar ao banco de dados MySQL
            conexao = mysql.connector.connect(
                host='localhost',        
                user='root',      
                password='',    
                database='senac'         
            )

            if conexao.is_connected():
                cursor = conexao.cursor()

                # Comando DELETE no SQL para remover a entrada com base nos parâmetros
                sql = '''
                DELETE FROM tabela_exemplo
                WHERE funcionario = %s AND portfolio = %s AND produto = %s AND servico = %s
                '''
                valores = (funcionario, portfolio, produto, servico)

                # Executar o comando com os parâmetros fornecidos
                cursor.execute(sql, valores)
                conexao.commit()  # Confirmar as alterações

                # Verificar se alguma linha foi afetada
                if cursor.rowcount > 0:
                    print("Entrada removida com sucesso!")
                else:
                    print("Nenhuma entrada encontrada com os parâmetros fornecidos.")
        
        except Error as erro:
            print(f"Erro ao remover a entrada: {erro}")
        
        finally:
            # Fechar a conexão com o banco de dados
            if conexao.is_connected():
                cursor.close()
                conexao.close()


# Exemplo de uso para remover uma entrada
# Vamos assumir que a tabela "tabela_exemplo" tem as colunas: 'funcionario', 'portfolio', 'produto' e 'servico'
Admin.remover_entrada("Luiz", "Financeiro", "ProdutoX", "ServicoY")