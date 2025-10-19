import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_apartados import conectar_banco_dados_apartados

from backend.constantes.bancos_dados import TABELA_APARTADOS

class Apartado():
    def __init__(self, data, codigo_produto, quantidade, motivo):
        self.data = data
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.motivo = motivo
    
    def inserir_apartado(self):

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


