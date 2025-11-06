import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_apartados import conectar_banco_dados_apartados

from backend.constantes.bancos_dados import TABELA_APARTADOS

class Apartado:
    """
    Representa um apartado.

    Attributes
    ----------
        data
            A data do apartado.
        codigo_produto
            O código do produto.
        quantidade
            A quantidade apartada.
        motivo
            O motivo do apartado.
    """

    def __init__(self, data, codigo_produto, quantidade, motivo):
        """
        Inicializa um novo apartado.

        Parameters
        ----------
            data    
                A data do apartado.
            codigo_produto
                O código do produto.
            quantidade
                A quantidade apartada.
            motivo
                O motivo do apartado.
        """

        self.data = data
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.motivo = motivo
    
    def inserir_apartado(self):
        """Insere um novo apartado no banco de dados."""

        conexao = conectar_banco_dados_apartados()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_APARTADOS} (data,
        codigo_produto,
        quantidade,
        motivo
        )
        VALUES (?, ?, ?, ?)
        """,
            (
                self.data,
                self.codigo_produto,
                self.quantidade,
                self.motivo
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_apartado(data, codigo_produto, quantidade):
        """
        Exclui um apartado do banco de dados.

        Parameters
        ----------
            data    
                A data do apartado.
            codigo_produto
                O código do produto.
            quantidade
                A quantidade apartada.
        Returns
        -------
            None
        """

        conexao = conectar_banco_dados_apartados()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_APARTADOS}
        WHERE data = ? AND codigo_produto = ? AND quantidade = ?
        """, (data, codigo_produto, quantidade)
        )

        conexao.commit()
        conexao.close()
    
    @staticmethod
    def buscar_apartado(data, codigo_produto, quantidade):
        """
        Busca um apartado no banco de dados.

        Parameters
        ----------
            data    
                A data do apartado.
            codigo_produto
                O código do produto.
            quantidade
                A quantidade apartada.
        Returns
        -------
            Se encontrado retorna seus dados, caso contrário retorna Falso.
        """

        try:
            conexao = conectar_banco_dados_apartados()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            SELECT * FROM {TABELA_APARTADOS}
            WHERE data = ? AND codigo_produto = ? AND quantidade = ?
            """, (data, codigo_produto, quantidade)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return Apartado(*resultado)
    
        except TypeError:
                return False
