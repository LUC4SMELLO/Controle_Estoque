import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_FORNECEDOR, TABELA_FORNECEDORES

def conectar_banco_de_dados_fornecedores():
    return sqlite3.connect(BANCO_DADOS_FORNECEDOR)

def criar_tabela_fornecedores():
    conexao = conectar_banco_de_dados_fornecedores()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_FORNECEDORES} (
        codigo_fornecedor VARCHAR(10) NOT NULL,
        razao_social VARCHAR(100),
        nome_fantasia VARCHAR(100),
        fornecedor_ativo INTERGER CHECK (fornecedor_ativo IN (0, 1)),
        cnpj VARCHAR(14),
        inscricao_estadual VARCHAR(9),
        logradouro VARCHAR(50),
        bairro VARCHAR(50),
        cidade VARCHAR(50),
        cep VARCHAR(8),
        estado VARCHAR(2),
        PRIMARY KEY (codigo_fornecedor)
    )
    """
    )

    conexao.commit()
    cursor.close()
