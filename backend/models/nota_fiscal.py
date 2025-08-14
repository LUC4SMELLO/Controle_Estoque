import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_nota_fiscal import conectar_banco_de_dados_nota_fiscal


class NotaFiscal:
    def __init__(self, numero_nota_fiscal, codigo_fornecedor, data_entrada):
        self.numero_nota_fiscal = numero_nota_fiscal
        self.codigo_fornecedor = codigo_fornecedor
        self.data_entrada = data_entrada

    def salvar_nota_fiscal(self):

        conexao = conectar_banco_de_dados_nota_fiscal()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaNotaFiscal (numero_nota_fiscal,
        codigo_fornecedor,
        data_entrada)
        VALUES (?, ?, ?)
        """,
            (self.numero_nota_fiscal, self.codigo_fornecedor, self.data_entrada)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_nota_fiscal(numero_nota_fiscal):

        conexao = conectar_banco_de_dados_nota_fiscal()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE * FROM TabelaNotaFiscal
        WHERE numero_nota_fiscal = ?
        """,
            (numero_nota_fiscal,)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_nota_fiscal_por_numero(numero_nota_fiscal):
        try:
            conexao = conectar_banco_de_dados_nota_fiscal()
            cursor = conexao.cursor()

            cursor.execute(
            """
            SELECT * FROM TabelaNotaFiscal
            WHERE numero_nota_fiscal = ?
            """,
                (numero_nota_fiscal,)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return NotaFiscal(*resultado)

        except TypeError:
            return False
