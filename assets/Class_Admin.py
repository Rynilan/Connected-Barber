#Obs: Não esquecer de alterar o Nome do banco de dados na hora do uso  

class Admin():
      def __init__(self, nome, email ,senha):
        self.nome = nome
        self.email = email
        self.__senha = senha 

    def Atualiza_atributo(self, atributo, valor):
        if (self, atributo):
            (self, atributo, valor)
            return (self, atributo)
        else:
            return f"O atributo '{atributo}' não existe."
     
    def Adiciona_ser(self, portifolio, funcionario,produto, servico):
        self.portifolio = portifolio
        self.funcionario = funcionario
        self.produto = produto
        self.servico = servico 
        ser == Adiciona_ser  

    #cod para Editar o ser
   
    def get_portifolio(self):
        return self.portifolio

    def set_portifolio(self):
        self.portifolio = portifolio:

    def get_funcionario(self):
        return self.funcionario

    def set_funcionario(self):
        self.funcionario = funcionario:

    def get_produto(self):
        return self.produto

    def set_produto(self):
        self.produto = produto:

    def get_servico(self):
        return self.servico

    def set_servico(self):
        self.servico = servico:

    #exclui o ser

    def Excluir_tudo():
        import mysql.connector
from mysql.connector import Error

def apagar_banco():
    try:
        # Conectar ao servidor MySQL OK
        conexao = mysql.connector.connect(
            host='localhost',        
            user='root',      
            password=''     
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            # Comando SQL para apagar o banco de dados da barbearia OK
            sql = "DROP DATABASE IF EXISTS senac"
            
            # Executar o comando OK
            cursor.execute(sql)
            print("Banco de dados 'senac' apagado com sucesso!")

    except Error as erro:
        print(f"Erro ao apagar o banco de dados: {erro}")

    finally:
        # Fechar a conexão com o banco de dados ao final da tarefa OK
        if conexao.is_connected():
            cursor.close()
            conexao.close()


    def Aumenta_nivel(Funcionario):
        Funcionario.set_nivel(self,"Adm")
        

    def Baixar_nivel(Funcionario):
        Funcionario.set_nivel(self,"Funcionario")

    def Remove_ser(Funcionário,Potfólio,Produto,Serviço):
        import mysql.connector
from mysql.connector import Error

def remover_entrada(funcionario, portfolio, produto, servico):
    try:
        # Conectar ao banco de dados MySQL OK
        conexao = mysql.connector.connect(
            host='localhost',        
            user='root',      
            password='',    
            database='senac'         
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            # Comando DELETE no SQL para remover a entrada com base nos parâmetros OK
            sql = '''
            DELETE FROM tabela_exemplo
            WHERE funcionario = %s AND portfolio = %s AND produto = %s AND servico = %s
            '''
            valores = (funcionario, portfolio, produto, servico)

            # Executar o comando com os parâmetros fornecidos
            cursor.execute(sql, valores)
            conexao.commit()  # Confirmar as alterações OK

            # Verificar se alguma linha foi afetada OK
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

# Exemplo para  uso
#remover_func("Luiz", "Financeiro", "ProdutoX", "ServiçoY")