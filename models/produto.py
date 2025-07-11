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

        conexao.commit()
        conexao.cursor()

    def atualizar_produto(
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
                codigo_produto
            )
        )

        conexao.commit()
        conexao.cursor()

cafe = Produto(
    codigo_produto = 1324,
    descricao = "Café da Roça",
    subdescricao = "Tradicional Moído 500g",
    produto_ativo = True,
    unidade_medida = "un",
    itens_embalagem = 20,
    codigo_barras = "7891234567890",
    grupo = "Mercearia",
    categoria = "Cafés",
    marca = "Sabor da Fazenda",
    itens_pallete = 1200,
    itens_lastro = 80
)

cafe.atualizar_produto(
    codigo_produto=1324,
    descricao="Café",
    subdescricao = "Tradicional Moído 500g",
    produto_ativo = True,
    unidade_medida = "un",
    itens_embalagem = 20,
    codigo_barras = "7891234567890",
    grupo = "Mercearia",
    categoria = "Cafés",
    marca = "Sabor da Fazenda",
    itens_pallete = 1200,
    itens_lastro = 80
    )

print(cafe.descricao)