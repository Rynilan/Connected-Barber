import mysql.connector


def create(valor):
    banco = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Connected_Barber"
    )
    cursor = banco.cursor()
    cursor.execute("insert into tabela_portfolios(id ,descricao)" +
                   "values (default, '{}');".format(valor))
    cursor.close()
    banco.close()


def update(descricao, id_user):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connected_barber"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE tabela_portfolios SET descricao = %s WHERE id = %d"
    mycursor.execute(sql, (descricao, id_user))
    mydb.commit()
    mycursor.close()
    mydb.close()


def select(id_portfolio):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",
        database="Connect_Barber"
    )
    # Conectando ao banco da barbearia OK
    cursor = mydb.cursor()
    results = None

    # Executando o SELECT
    query = "SELECT * FROM tabela_portfolios WHERE id = %d"
    cursor.execute(query, (id_portfolio,))

    results = cursor.fetchall()

    # Fechar conexão OK
    cursor.close()
    mydb.close()

    # Retornando os resultados da seleção
    return results


def delete(id_portfolio):

    # Configurações e conexão com o banco de dados da barbearia OK
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connected_Barber"
    )
    # Conectando ao banco de dados
    cursor = mydb.cursor()

    # Executando a função de  DELETE
    query = "DELETE FROM tabela_portfolios WHERE id = %d"
    cursor.execute(query, (id_portfolio,))

    # Confirmando se o id foi deletado
    mydb.commit()

    # Fechando o cursor e a conexão com o banco da barbearia OK
    cursor.close()
    mydb.close()
