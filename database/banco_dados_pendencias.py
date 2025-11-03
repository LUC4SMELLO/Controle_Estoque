import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_PENDENCIAS, TABELA_PENDENCIAS


def conectar_banco_de_dados_pendencias():
    return sqlite3.connect(BANCO_DADOS_PENDENCIAS)


def criar_tabela_pendencias():

    conexao = conectar_banco_de_dados_pendencias()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_PENDENCIAS} (
    cupom VARCHAR(10),
    data_ocorrencia VARCHAR(10),
    codigo_cliente VARCHAR(200),
    razao_social VARCHAR(200),
    cidade VARCHAR(20),
    vendedor VARCHAR(10),
    codigo_produto VARCHAR(10),
    quantidade VARCHAR(10)
    )
    """
    )

    conexao.commit()
    conexao.close()
