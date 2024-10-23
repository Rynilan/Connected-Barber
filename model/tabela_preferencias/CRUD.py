from mysql.connector import connect


def conectar():
    banco = connect(
        password='',
        username='root',
        database='connected_barber',
        host='localhost'
    )
    return banco, banco.cursor()


def create(descricao, fk_cliente):
    banco, cursor = conectar()
    cursor.execute('insert into tabela_preferencias values (default, %s, %s);',
                   (descricao, fk_cliente))
    banco.commit()
    cursor.close()
    banco.close()


def select(cliente):
    banco, cursor = conectar()
    cursor.execute('select * from tabela_preferencias where fk_cliente = %s;',
                   (cliente, ))
    resultados = cursor.fetchall()
    cursor.close()
    banco.close()
    return resultados


def update(id, descricao):
    banco, cursor = conectar()
    cursor.execute('update tabela_preferencias set {} where id = {};'.format(
        'descricao = ' + descricao, id))
    banco.commit()
    cursor.close()
    banco.close()


def delete(id):
    banco, cursor = conectar()
    cursor.execute('delete from tabela_preferencias where id = %d' (id, ))
    banco.commit()
    cursor.close()
    banco.close()
