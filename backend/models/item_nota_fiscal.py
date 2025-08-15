import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_itens_nota import conectar_banco_de_dados_itens_nota_fiscal

class ItemNotaFiscal:
    def __init__(
        self,
        id_item_nota,
        numero_nota_fiscal,
        codigo_produto,
        quantidade,
        preco_unitario,
        valor_total
    ):      
        self.id_item_nota = id_item_nota
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
        INSERT INTO TabelaItensNotaFiscal (id_item_nota
        numero_nota_fiscal,
        codigo_produto,
        quantidade,
        preco_unitario,
        valor_total)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                self.id_item_nota,
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
    def buscar_item_nota_por_codigo(id_item_nota):
        try:
            conexao = conectar_banco_de_dados_itens_nota_fiscal()
            cursor = conexao.cursor()

            cursor.execute(
            """
            SELECT * FROM TabelaItensNotaFiscal
            WHERE id_item_nota = ?
            """, (id_item_nota,)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return ItemNotaFiscal(*resultado)
        
        except TypeError:
            return False
