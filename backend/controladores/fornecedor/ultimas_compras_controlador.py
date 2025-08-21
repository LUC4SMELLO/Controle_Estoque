from backend.models.item_nota_fiscal import ItemNotaFiscal

from database.banco_dados_itens_nota import conectar_banco_de_dados_itens_nota_fiscal

def retornar_ultimas_compras_fornecedor(codigo_fornecedor):

    try:
        conexao = conectar_banco_de_dados_itens_nota_fiscal()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT * FROM TabelaItensNotaFiscal
        WHERE codigo_fornecedor = ?
        """, (codigo_fornecedor,)
        )

        resultado = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return resultado

    except TypeError:
        return False