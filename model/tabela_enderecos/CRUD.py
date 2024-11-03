import mysql.connector


def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connect_Barber"
    )

    mycursor = mydb.cursor()
    return mydb, mycursor


def insert(self, pais, estado, cidade, cep, complemento):
    mydb, mycursor = conectar()
    sql = str("INSERT INTO tabela_enderecos (fk_pais,fk_estado,fk_cidade," +
              "cep,complemento) VALUES (%d, %d, %d, %s, %s, %s)")
    val = (pais, estado, cidade, cep, complemento)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute('SELECT MAX(id) FROM tabela_enderecos;')
    ultimo_registro = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return ultimo_registro


def select(identificador):
    mydb, mycursor = conectar()
    mycursor.execute("SELECT * FROM tabela_enderecos where id = {}".format(
        identificador
    ))
    resultados = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return resultados


def delete(id):
    mydb, mycursor = conectar()
    sql = "DELETE FROM tabela_enderecos WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()
    mycursor.close()
    mydb.close()


def update(identificador, campos, valores):
    mydb, mycursor = conectar()
    if not len(campos) == len(valores):
        raise ValueError('dimensões diferentes entre campos e valores.')
    parametros_sql = ''
    for indice in range(0, len(campos)):
        parametros_sql += '{} = {}, '.format(campos[indice],
                                             valores[indice])
    parametros_sql.removesuffix(', ')
    mycursor.execute('update tabela_enderecos set {} where id = {};'.format(
        parametros_sql, identificador
    ))
    mycursor.close()
    mydb.close()
