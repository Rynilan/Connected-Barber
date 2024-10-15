import mysql.connector
def update (descricao,id_user): 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Connected_barber"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE tabela_portfolios SET descricao = %s WHERE id = %d"

    mycursor.execute(sql)

    mydb.commit()

    mycursor.close()
    mydb.close()
