import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_APARTADOS, TABELA_APARTADOS

def conectar_banco_dados_apartados():
    return sqlite3.connect(BANCO_DADOS_APARTADOS)

def criar_banco_dados_apartados():
    
    conexao = conectar_banco_dados_apartados()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_APARTADOS} (
    data VARCHAR(10),
    codigo_produto VARCHAR(10),
    quantidade VARCHAR(10),
    motivo VARCHAR(100))
    """
    )

    conexao.commit()
    conexao.close()
