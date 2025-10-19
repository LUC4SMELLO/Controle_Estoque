from database.banco_dados_produtos import conectar_banco_de_dados_produtos

from backend.constantes.bancos_dados import TABELA_PRODUTOS

def produto_existe(codigo_produto):

    conexao = conectar_banco_de_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    SELECT 1 FROM {TABELA_PRODUTOS}
    WHERE codigo_produto = ?
    """, (codigo_produto,)
    )

    existe = cursor.fetchone()

    conexao.commit()
    conexao.close()

    if existe:
        return True, "Produto Já Existe."
    else:
        return False, "Produto Não Encontrado."
    