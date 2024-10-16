from mysql.connector import connect


def create(id_portfolio, endereco):
    # Srtª Paiva
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
