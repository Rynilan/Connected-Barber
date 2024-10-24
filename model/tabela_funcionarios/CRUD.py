from mysql.connector import connect


def conectar():
    banco = connect(
        host='localhost',
        username='root',
        password='',
        database='Connected_Barber'
    )
    return banco, banco.cursor()


def create(fk_usuario, fk_portfolio, fk_barbearia):
    banco, cursor = conectar()
    cursor.execute(
        'insert into tabela_funcionarios values (default, %s, %s, %d, %s, %s)',
        (fk_usuario, fk_portfolio, fk_barbearia)
    )
    banco.commit()
    cursor.close()
    banco.close()


def select(fk_usuario):
    banco, cursor = conectar()
    cursor.execute(
        'select * from tabela_funcionarios where fk_usuario = %d;',
        (fk_usuario, )
    )
    cursor.close()
    banco.close()


def update(fk_usuario, campos, valores):
    if not len(campos) == len(valores):
        raise ValueError('dimensões diferentes entre campos e valores.')
    parametro = ''
    for indice in range(0, len(campos)):
        parametro += "{} = {}, ".format(campos[indice], valores[indice])
    banco, cursor = conectar()
    cursor.execute(
        'update tabela_funcionarios set %s where fk_usuario = %s;',
        (parametro, fk_usuario)
    )
    banco.commit()
    cursor.close()
    banco.close()


def delete(fk_usuario):
    banco, cursor = conectar()
    cursor.execute(
        'delete from tabela_funcionarios where fk_usuario = %d;',
        (fk_usuario, )
    )
    banco.commit()
    cursor.close()
    banco.close()
