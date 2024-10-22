from mysql.connector import connect


def create(id_portfolio, endereco):
    banco = connect(
      host="localhost",
      user="root",
      password="",
      database="Connected_Barber"
    )
    cursor = banco.cursor()
    cursor.execute("insert into tabela_fotos(id,endereco,fk_portfolio)" +
                   "values (default, '{}', {})".format(endereco, id_portfolio))
    cursor.close()
    banco.close()


def update(id_foto, campos, valores):
    mydb = connect(
        host="localhost",
        user="root",
        password="",
        database="Conected_Barber"
    )
    mycursor = mydb.cursor()
    formatar = ""
    for indice in range(0, len(valores)):
        formatar += "{}={}, ".format(campos[indice], valores[indice])
    formatar.removesuffix(", ")
    mycursor.execute("update from tabela_fotos set {} where id = {}".format(
        formatar, id_foto))
    mydb.commit()
    mycursor.close()
    mydb.close()
