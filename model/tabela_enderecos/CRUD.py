from connect import conectar


class conexao():
    def salvar(self, pais, estado, cidade, cep, complemento):
        try:
            mydb, mycursor = conectar()
            sql = str("INSERT INTO endereco (fk_pais,fk_estado,fk_cidade,cep" +
                      ",complemento) VALUES (%d, %d, %d, %s, %s, %s)")
            val = (pais, estado, cidade, cep, complemento)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
            mydb.close()
        except:
            print("Erro ao adicionar o Endereço")  # Futuramente remover print.

    def lista():
        try:
            mydb, mycursor = conectar()
            mycursor.execute("SELECT * FROM endereco")
            mycursor.close()
            mydb.close()
            return mycursor.fetchall()
        except:
            print("Erro ao conectar a tabela")

    def apagar(id):
        try:
            mydb, mycursor = conectar()
            sql = "DELETE FROM endereco WHERE id = %s"
            mycursor.execute(sql, (id,))
            mydb.commit()
            mycursor.close()
            mydb.close()
        except:
            print("Erro ao deletar o endereço da barbearia")

    def alterar(identificador, campos, valores):
        mydb, mycursor = conectar()
        if len(campos) != len(valores) and campos and valores:
            print("erro, tamanho dos campos difere dos valores")
        parametros_sql = ''
        for indice in range(0, len(campos)):
            parametros_sql += '{} = {}, '.format(campos[indice],
                                                 valores[indice])
        parametros_sql.removesuffix(', ')
        mycursor.execute('update tabela_endereco set {} where id = {};'.format(
            parametros_sql, identificador
        ))
        mycursor.close()
        mydb.close()
