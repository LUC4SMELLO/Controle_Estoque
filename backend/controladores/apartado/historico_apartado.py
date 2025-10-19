from database.banco_dados_apartados import conectar_banco_dados_apartados

def buscar_historico_apartados_back(data="", codigo_produto="", motivo=""):

    conexao = conectar_banco_dados_apartados()
    cursor = conexao.cursor()

    cursor.execute("ATTACH DATABASE 'produtos.db' AS produtos")

    consulta_sql = """
    SELECT ap.data, ap.codigo_produto, p.descricao, ap.quantidade, ap.motivo
    FROM apartados AS ap
    INNER JOIN produtos AS p
    ON ap.codigo_produto = p.codigo_produto
    """
    parametros = []

    if data:
        consulta_sql += " AND ap.data = ?"
        parametros.append(data)
    
    if codigo_produto:
        consulta_sql += " AND ap.codigo_produto = ?"
        parametros.append(codigo_produto)

    if motivo:
        consulta_sql += " AND ap.motivo = ?"
        parametros.append(motivo)

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado
