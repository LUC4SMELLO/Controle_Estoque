import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_itens_nota import conectar_banco_de_dados_itens_nota_fiscal

class ItemNotaFiscal:
    def __init__(
        self,
        numero_nota_fiscal,
        codigo_produto,
        quantidade,
        preco_unitario,
        valor_total
    ):      
        self.numero_nota_fiscal = numero_nota_fiscal
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.valor_total = valor_total

    def salvar_item_nota_fiscal(self):

        conexao = conectar_banco_de_dados_itens_nota_fiscal()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaItensNotaFiscal (numero_nota_fiscal,
        codigo_produto,
        quantidade,
        preco_unitario,
        valor_total)
        VALUES (?, ?, ?, ?, ?)
        """,
            (
                self.numero_nota_fiscal,
                self.codigo_produto,
                self.quantidade,
                self.preco_unitario,
                self.valor_total
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_item_nota_por_codigo(numero_nota_fiscal, codigo_produto):
        try:
            conexao = conectar_banco_de_dados_itens_nota_fiscal()
            cursor = conexao.cursor()

            cursor.execute(
            """
            SELECT * FROM TabelaItensNotaFiscal
            WHERE numero_nota_fiscal = ? AND codigo_produto = ?
            """, (numero_nota_fiscal, codigo_produto)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return ItemNotaFiscal(*resultado)
        
        except TypeError:
            return False
