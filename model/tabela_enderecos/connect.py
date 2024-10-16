import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connect_Barber"
    )

    mycursor = mydb.cursor()
    print("Conectado no banco com sucesso!")

except:
    print("Conexao falhou!")
