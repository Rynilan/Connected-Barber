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
