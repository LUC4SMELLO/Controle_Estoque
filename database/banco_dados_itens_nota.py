import sqlite3

def conectar_banco_de_dados_itens_nota_fiscal():
    return sqlite3.connect("TabelaItensNotaFiscal.db")

def criar_tabela_itens_nota_fiscal():

    conexao = conectar_banco_de_dados_itens_nota_fiscal()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaItensNotaFiscal (
        numero_nota_fiscal VARCHAR(9),
        codigo_produto VARCHAR(6),
        quantidade VARCHAR(10),
        preco_unitario VARCHAR(10),
        valor_total VARCHAR(10),
        PRIMARY KEY (id_item_nota),
        FOREIGN KEY (numero_nota_fiscal) REFERENCES TabelaNotaFiscal(numero_nota_fiscal),
        FOREIGN KEY (codigo_produto) REFERENCES TabelaProdutos(codigo_produto)
    )
    """
    )

    conexao.commit()
    conexao.close()