import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_PRODUTOS, TABELA_PRODUTOS

def conectar_banco_de_dados_produtos():
    return sqlite3.connect(BANCO_DADOS_PRODUTOS)

def criar_tabela_produtos():
    conexao = conectar_banco_de_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_PRODUTOS} (
        codigo_produto VARCHAR(10) NOT NULL,
        descricao VARCHAR(50),
        subdescricao VARCHAR(50),
        produto_ativo INTEGER CHECK (produto_ativo IN (0, 1)),
        unidade_medida VARCHAR(30),
        itens_embalagem INTEGER,
        codigo_barras VARCHAR(13),
        grupo VARCHAR(30),
        categoria VARCHAR(30),
        marca VARCHAR(30),
        itens_pallete INTEGER,
        itens_lastro INTEGER,
        quantidade_estoque INTEGER,
        PRIMARY KEY (codigo_produto)
    )
    """
    )

    conexao.commit()
    cursor.close()
