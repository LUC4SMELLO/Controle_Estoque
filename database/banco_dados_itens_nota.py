import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_ITENS_NOTA_FISCAL, TABELA_ITENS_NOTA_FISCAL

def conectar_banco_de_dados_itens_nota_fiscal():
    return sqlite3.connect(BANCO_DADOS_ITENS_NOTA_FISCAL)

def criar_tabela_itens_nota_fiscal():

    conexao = conectar_banco_de_dados_itens_nota_fiscal()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_ITENS_NOTA_FISCAL} (
        data_entrada VARCHAR(10),
        numero_nota_fiscal VARCHAR(9),
        codigo_fornecedor VARCHAR(6),
        codigo_produto VARCHAR(6),
        descricao VARCHAR(50),
        quantidade VARCHAR(10),
        preco_unitario VARCHAR(10),
        preco_total VARCHAR(10),
        FOREIGN KEY (numero_nota_fiscal) REFERENCES nota_fiscal(numero_nota_fiscal),
        FOREIGN KEY (codigo_produto) REFERENCES produtos(codigo_produto),
        FOREIGN KEY (codigo_fornecedor) REFERENCES fornecedor(codigo_fornecedor)
    )
    """
    )

    conexao.commit()
    conexao.close()