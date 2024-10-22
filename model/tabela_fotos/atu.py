import mysql.conector
def atualizar (id_foto,campos,valores):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Conected_Barber"
    )
    
    mycursor = mydb.cursor()
    formatar = ""
    for indice in range (0,len(valores)):
        formatar +="{}={}, ".format (campos[indice],valores[indice])
    formatar.removesuffix(", ")
    mycursor.execute("update from tabela_fotos set {} where id = {} ".format (formatar,id_foto))
    mydb.commit()
    mycursor.close()
    mydb.close()
