import mysql.connector

def create(valor):
    banco = mysql.connector.connect(
       host="localhost", 
       user="root",
      password="",
      database="Connected_Barber"
    )
    cursor = banco.cursor()
    cursor.execute( " insert into tabela_portfolios(id,descricao ) values (default,'{}');".format(valor)
    cursor.close()
    banco.close()