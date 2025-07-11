import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    def salvar_produto(
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
        itens_lastro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
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
            ),
        )
