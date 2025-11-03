import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from backend.constantes.bancos_dados import TABELA_PENDENCIAS

class Pendencia:
    def __init__(
            self,
            cupom,
            data_ocorrencia,
            codigo_cliente,
            razao_social,
            cidade,
            vendedor,
            codigo_produto,
            quantidade
    ):
        self.cupom = cupom
        self.data_ocorrencia = data_ocorrencia
        self.codigo_cliente = codigo_cliente
        self.razao_social = razao_social
        self.cidade = cidade 
        self.vendedor = vendedor
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade

    def salvar_pendencia(self):

        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_PENDENCIAS} (cupom,
        data_ocorrencia,
        codigo_cliente,
        razao_social,
        cidade,
        vendedor,
        codigo_produto,
        quantidade
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.cupom,
                self.data_ocorrencia,
                self.codigo_cliente,
                self.razao_social,
                self.cidade,
                self.vendedor,
                self.codigo_produto,
                self.quantidade
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_pendencia(cupom):

        conexao = conectar_banco_de_dados_pendencias()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_PENDENCIAS}
        WHERE cupom  = ?
        """, (cupom,)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_pendencia(cupom):
        try:
            conexao = conectar_banco_de_dados_pendencias()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            SELECT * FROM {TABELA_PENDENCIAS}
            WHERE cupom = ?
            """, (cupom,)
            )
            
            resultado = cursor.fetchall()

            conexao.commit()
            conexao.close()

            return resultado

        except Exception:
            return False
