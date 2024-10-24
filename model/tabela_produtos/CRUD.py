import mysql.connector


def conectar():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Connected_Barber"
    )

    mycursor = mydb.cursor()
    return mydb, mycursor
# id, fk_barbearia, nome, preco, tempo_estimado, fk_info.


def insert(fk_barbearia, nome, preco, marca, validade, fk_info):
    mydb, mycursor = conectar()
    sql = str("INSERT INTO tabela_produtos values (default, %d, %s," +
              "%.2f, %d, %s, %d);")
    val = (fk_barbearia, nome, preco, marca, validade, fk_info)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def select(identificador):
    mydb, mycursor = conectar()
    mycursor.execute("SELECT * FROM tabela_produtos where id = {}".format(
        identificador
    ))
    resultados = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return resultados


def delete(id):
    mydb, mycursor = conectar()
    sql = "DELETE FROM tabela_produtos WHERE id = %d"
    mycursor.execute(sql, (id,))
    mydb.commit()
    mycursor.close()
    mydb.close()


def update(identificador, campos, valores):
    mydb, mycursor = conectar()
    if len(campos) != len(valores) and campos and valores:
        raise ValueError('dimensões diferentes entre campos e valores.')
    parametros_sql = ''
    for indice in range(0, len(campos)):
        parametros_sql += '{} = {}, '.format(campos[indice],
                                             valores[indice])
    parametros_sql.removesuffix(', ')
    mycursor.execute('update tabela_produtos set {} where id = {};'.format(
        parametros_sql, identificador
    ))
    mycursor.close()
    mydb.close()
