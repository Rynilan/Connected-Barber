from mysql.connector import connect, connection, cursor


def conectar() -> tuple[cursor.MySQLCursor, connection.MySQLConnection]:
    banco = connect(
        host='localhost',
        username='root',
        password='',
        database='Connected_Barber'
    )
    cursor = banco.cursor()
    return (cursor, banco)


def select(
    nome: str,
    campos: tuple[str] = '*'
) -> list[str]:
    """ Retorna os dados da tabela barbearia cujo o nome coincide com o dado.
    """
    cursor, banco = conectar()
    cursor.execute(
        'select ' + campos + ' from tabela_barbearias join tabela_endereco j' +
        'oin tabela_portfolios_barbearia on tabela_barbearias.fk_endereco = ' +
        'tabela_endereco.id and tabela_barbearias.fk_portfolio = tabela_port' +
        'folios_barbearias.id where nome = "' + nome + '";'
    )
    resultados = cursor.fetchall()
    cursor.close()
    banco.close()
    return resultados


def update(
    campos: tuple[str],
    valores: tuple[str],
    chave: str
) -> None:
    cursor, banco = conectar()
    if len(valores) != len(campos):
        raise ValueError("Tamanhos de campos e valores dados diferem")
    else:
        valores = str(tuple('{} = {}'.format(campos[indice], valores[indice])
                            for indice in range(0, len(valores))))
        valores = valores.removeprefix('(').removesuffix(')')
    cursor.execute(
        'update tabela_barbearias set {}'.format(valores) + 'where nome = "' +
        chave + '";'
    )
