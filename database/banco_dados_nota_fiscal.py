import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_NOTA_FISCAL, TABELA_NOTAS_FISCAL


def conectar_banco_de_dados_nota_fiscal():
    return sqlite3.connect(BANCO_DADOS_NOTA_FISCAL)


def criar_tabela_nota_fiscal():

    conexao = conectar_banco_de_dados_nota_fiscal()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_NOTAS_FISCAL} (
        numero_nota_fiscal VARCHAR(9) NOT NULL,
        codigo_fornecedor VARCHAR(6),
        data_entrada VARCHAR(10),
        PRIMARY KEY (numero_nota_fiscal),
        FOREIGN KEY (codigo_fornecedor) REFERENCES TabelaFornecedores(codigo_fornecedor)
    )
    """
    )

    conexao.commit()
    conexao.close()
