import sqlite3

def conectar_banco_dados_apartados():
    return sqlite3.connect("TabelaApartados.db")

def criar_banco_dados_apartados():
    
    conexao = conectar_banco_dados_apartados()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaApartados (
    data VARCHAR(10),
    codigo_produto VARCHAR(10),
    quantidade VARCHAR(10),
    motivo VARCHAR(100))
    """
    )

    conexao.commit()
    conexao.close()
