import mysql.connector


def delete(email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connected_Barber"
    )
    mycursor = mydb.cursor()
    mycursor.execute("delete from tabel_usuarios where email=%s", email)
    mycursor.close()
    mydb.close()


def insert(val):
    """ val deve ser uma tupla contendo os seguintes elementos:
        string - nome do usuário.
        string - email do usuário.
        string - senha do usuário.
        datetime - data de nascimento do usuário.
        string - telefone do usuário.
        string - cep do usuário.
        string - nível do usuário.
    """
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Connected_Barber"
    )
    mycursor = mydb.cursor()
    sql = str("INSERT INTO tabela_usuarios(nome,email,senha,data_de_nascimen" +
              "to,telefone,cep,nivel) values (%s, %s,%s,%s,%s,%s,%s)")
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def select(email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Connected_Barber"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM tabela_usuarios where email="+email)
    resultados = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return resultados


def update(campos, valores, email):
    mydb = mysql.connector.connect(
        host="root",
        user="connected_barber",
        password="",
        database="tabela_barbearias"
    )
    mycursor = mydb.cursor()
    formatada = ""
    for indice in range(0, len(campos)):
        formatada += campos[indice] + " = " + valores[indice] + ", "
    formatada.removesuffix(", ")
    sql = "UPDATE tabela_usuarios SET {} where email= '{}'".format(
        formatada, email)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
