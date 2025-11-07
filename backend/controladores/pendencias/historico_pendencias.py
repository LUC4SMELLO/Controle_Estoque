from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from backend.constantes.bancos_dados import TABELA_PENDENCIAS

def buscar_historico_pendencias_back(
        cupom="",
        data_ocorrencia="",
        codigo_cliente="",
        razao_social="",
        cidade="",
        vendedor="",
        codigo_produto="",
        quantidade=""
    ):

    conexao = conectar_banco_de_dados_pendencias()
    cursor = conexao.cursor()

    consulta_sql = f"""
    SELECT cupom,
    data_ocorrencia,
    codigo_cliente,
    razao_social,
    cidade,
    vendedor,
    codigo_produto,
    quantidade
    FROM {TABELA_PENDENCIAS}
    WHERE 1=1
    """
    parametros = []

    if cupom:
        consulta_sql += " AND cupom = ?"
        parametros.append(cupom)

    if data_ocorrencia:
        consulta_sql += " AND data_ocorrencia = ?"
        parametros.append(data_ocorrencia)
    
    if codigo_cliente:
        consulta_sql += " AND codigo_cliente = ?"
        parametros.append(codigo_cliente)

    if razao_social:
        consulta_sql += " AND razao_social = ?"
        parametros.append(razao_social)

    if cidade:
        consulta_sql += " AND cidade = ?"
        parametros.append(cidade)

    if vendedor:
        consulta_sql += " AND vendedor = ?"
        parametros.append(vendedor)

    if codigo_produto:
        consulta_sql += " AND codigo_produto = ?"
        parametros.append(codigo_produto)

    if quantidade:
        consulta_sql += " AND quantidade = ?"
        parametros.append(quantidade)


    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado