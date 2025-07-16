import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_produtos import conectar_banco_de_dados_produtos


class Produto:
    def __init__(
        self,
        codigo_produto,
        descricao,
        subdescricao,
        produto_ativo,
        unidade_medida,
        itens_embalagem,
        codigo_barras,
        grupo,
        categoria,
        marca,
        itens_pallete,
        itens_lastro,
    ):
        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.subdescricao = subdescricao
        self.produto_ativo = produto_ativo
        self.unidade_medida = unidade_medida
        self.itens_embalagem = itens_embalagem
        self.codigo_barras = codigo_barras
        self.grupo = grupo
        self.categoria = categoria
        self.marca = marca
        self.itens_pallete = itens_pallete
        self.itens_lastro = itens_lastro
        self.quantidade_estoque = 0

    def salvar_produto(self):

        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaProdutos (codigo_produto,
        descricao,
        subdescricao,
        produto_ativo,
        unidade_medida,
        itens_embalagem,
        codigo_barras,
        grupo,
        categoria,
        marca,
        itens_pallete,
        itens_lastro,
        quantidade_estoque)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.codigo_produto,
                self.descricao,
                self.subdescricao,
                self.produto_ativo,
                self.unidade_medida,
                self.itens_embalagem,
                self.codigo_barras,
                self.grupo,
                self.categoria,
                self.marca,
                self.itens_pallete,
                self.itens_lastro,
                self.quantidade_estoque
            ),
        )

        conexao.commit()
        conexao.close()

    def atualizar_produto(self):

        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        UPDATE TabelaProdutos
        SET descricao = ?,
        subdescricao = ?,
        produto_ativo = ?,
        unidade_medida = ?,
        itens_embalagem = ?,
        codigo_barras = ?,
        grupo = ?,
        categoria = ?,
        marca = ?,
        itens_pallete = ?,
        itens_lastro = ?
        WHERE codigo_produto = ?
        """,
            (
                self.descricao,
                self.subdescricao,
                self.produto_ativo,
                self.unidade_medida,
                self.itens_embalagem,
                self.codigo_barras,
                self.grupo,
                self.categoria,
                self.marca,
                self.itens_pallete,
                self.itens_lastro,
                self.codigo_produto
            )
        )

        conexao.commit()
        conexao.close()
    
    @staticmethod
    def excluir_produto(codigo_produto):
        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE FROM TabelaProdutos
        WHERE codigo_produto = ?
        """, (codigo_produto,)
        )

        conexao.commit()
        conexao.close()
    
    @staticmethod
    def buscar_produto(codigo_produto):
        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT * FROM TabelaProdutos
        WHERE codigo_produto = ?
        """, (codigo_produto,)
        )

        resultado = cursor.fetchone()

        conexao.commit()
        conexao.close()

        return resultado
    
    def entrada_estoque_produto(self, valor: int):
        self.quantidade_estoque += valor

        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        UPDATE TabelaProdutos
        SET quantidade_estoque = ?
        WHERE codigo_produto = ?
        """, (self.quantidade_estoque, self.codigo_produto)
        )

        conexao.commit()
        conexao.close()
    

    def saida_estoque_produto(self, valor: int):
        self.quantidade_estoque -= valor
    
    @staticmethod
    def listar_todos_produtos():
        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT * FROM TabelaProdutos
        """
        )

        resultado = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return resultado