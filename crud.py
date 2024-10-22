from conn import *

def create(id, nome, preco):
        
        sql = str("INSERT INTO tabela_servicos (fk_id,fk_nome,fk_preco," ) 
        VALUES ( %s, %s, %s)"
        val = (id, nome, preco,)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()


def select(identificador):

        mycursor.execute("SELECT * FROM tabela_servicos where id = {}".format(
            identificador
        ))
        mycursor.close()
        mydb.close()
        return mycursor.fetchall()



def delete(id):

        sql = "DELETE FROM tabela_servicos WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()
        mycursor.close()
        mydb.close()


def update(identificador, campos, valores):

    if len(campos) != len(valores) and campos and valores:
        print("erro, tamanho dos campos difere dos valores")
        return
    parametros_sql = ''
    for indice in range(0, len(campos)):
        parametros_sql += '{} = {}, '.format(campos[indice],
                                             valores[indice])
    parametros_sql.removesuffix(', ')
    mycursor.execute('update tabela_servicos set {} where id = {};'.format(
        parametros_sql, identificador
    ))
    mycursor.close()
    mydb.close()