import mysql.connector


def conectar():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Connect_Barber"
        )

        mycursor = mydb.cursor()
        print("Conectado no banco com sucesso!")
        return mydb, mycursor
    except:
        print("Conexao falhou!")
