import sqlite3

def conectar_banco_de_dados_nota_fiscal():
    return sqlite3.connect("TabelaNotaFiscal.db")

def criar_tabela_nota_fiscal():

    conexao = conectar_banco_de_dados_nota_fiscal()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaNotaFiscal.db (
        numero_nota_fiscal VARCHAR(9) NOT NULL,
        codigo_fornecedor VARCHAR(6),
        data_entrada VARCHAR (10),
        PRIMARY KEY (numero_nota_fiscal)
        )
    """
    )