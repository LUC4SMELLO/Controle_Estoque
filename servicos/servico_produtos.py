from database.banco_dados_produtos import conectar_banco_de_dados_produtos

def produto_exite(codigo_produto):

    conexao = conectar_banco_de_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaProdutos
    WHERE codigo_produto = ?
    """, (codigo_produto,)
    )

    existe = cursor.fetchone()

    conexao.commit()
    conexao.close()

    if existe:
        return True, "Produto Existe."
    else:
        return False, "Produto Não Encontrado."
    