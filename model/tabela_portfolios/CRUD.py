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
