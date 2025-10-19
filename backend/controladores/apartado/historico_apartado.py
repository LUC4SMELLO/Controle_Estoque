from database.banco_dados_apartados import conectar_banco_dados_apartados

def buscar_historico_apartados_back(data="", codigo_produto="", motivo=""):

    conexao = conectar_banco_dados_apartados()
    cursor = conexao.cursor()

    cursor.execute("ATTACH DATABASE 'TabelaProdutos.db' AS TabelaProdutos")

    consulta_sql = """
    SELECT ap.data, ap.codigo_produto, p.descricao, ap.quantidade, ap.motivo
    FROM TabelaApartados AS ap
    INNER JOIN TabelaProdutos AS p
    ON ap.codigo_produto = p.codigo_produto
    """
    parametros = []

    if data:
        consulta_sql += " AND data = ?"
        parametros.append(data)
    
    if codigo_produto:
        consulta_sql += " AND codigo_produto = ?"
        parametros.append(codigo_produto)

    if motivo:
        consulta_sql += " AND motivo = ?"
        parametros.append(motivo)

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado
