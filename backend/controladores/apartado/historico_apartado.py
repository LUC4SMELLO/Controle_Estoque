from database.banco_dados_apartados import conectar_banco_dados_apartados

def buscar_historico_apartados_back(data="", codigo_produto="", motivo=""):

    conexao = conectar_banco_dados_apartados()
    cursor = conexao.cursor()

    consulta_sql = """
    SELECT data, codigo_produto, quantidade, motivo FROM TabelaApartados WHERE 1=1
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
