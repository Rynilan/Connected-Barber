from model.tabela_barbearias.CRUD import insert as insert_barbearia
from model.tabela_enderecos.CRUD import insert as insert_endereco
from model.tabela_portfolios.CRUD import insert as insert_portfolio
from control.validadores.validacao_cep import validacao_cep
from control.validadores.validacao_nome import validacao_nome
from control.formatadores.formatador_nome import formatador_nome_entrada


# função posta em suspensão, necessária análise para resolução de problema.
def cadastrar_barbearia(
    nome: str,
    pais: str,
    estado: str,
    cidade: str,
    cep: str,
    complemento: str,
) -> None:
    """ Nota, país, estado e cidade são chaves estrangeiras de suas respectivas
        tabelas. """
    nome = formatador_nome_entrada(nome)
    if not (validacao_nome(nome) or validacao_cep(cep)):
        raise ValueError("Valores nome ou CEP não são válidos.")
    nome: str
    id_portfolio = insert_portfolio(
        'Somos a barbearia {}, seja bem vindo!'.format(nome.capitalize())
    )
    id_endereco = insert_endereco(pais, estado, cidade, cep, complemento)
    insert_barbearia((nome, id_portfolio, id_endereco))
