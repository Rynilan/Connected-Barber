from mysql.connector import connect


def conectar():
    banco = connect(
        host='localhost',
        username='root',
        password='',
        database='Connected_Barber'
    )
    return banco, banco.cursor()


def create(fk_cliente, fk_servico, fk_funcionario, data, situacao):
    banco, cursor = conectar()
    cursor.execute(
        'insert into tabela_agendamentos values (default, %s, %s, %d, %s, %s)',
        (fk_cliente, fk_funcionario, fk_servico, data, situacao)
    )
    banco.commit()
    cursor.close()
    banco.close()


def select(id):
    banco, cursor = conectar()
    cursor.execute(
        'select * from tabela_agendamentos where id = %d;', (id, )
    )
    cursor.close()
    banco.close()


def update(id, campos, valores):
    if not len(campos) == len(valores):
        raise ValueError('dimensões diferentes entre campos e valores.')
    parametro = ''
    for indice in range(0, len(campos)):
        parametro += "{} = {}, ".format(campos[indice], valores[indice])
    banco, cursor = conectar()
    cursor.execute(
        'update tabela_agendamentos set %s where id = %d;', (parametro, id)
    )
    banco.commit()
    cursor.close()
    banco.close()


def delete(id):
    banco, cursor = conectar()
    cursor.execute(
        'delete from tabela_agendamentos where id = %d;', (id, )
    )
    banco.commit()
    cursor.close()
    banco.close()
