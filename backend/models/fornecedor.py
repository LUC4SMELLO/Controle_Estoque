import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.banco_dados_fornecedores import conectar_banco_de_dados_fornecedores

from backend.constantes.bancos_dados import TABELA_FORNECEDORES

class Fornecedor:
    def __init__(
            self,
            codigo_fornecedor,
            razao_social,
            nome_fantasia,
            fornecedor_ativo,
            cnpj,
            inscricao_estadual,
            logradouro,
            bairro,
            cidade,
            cep,
            estado,

    ):
        self.codigo_fornecedor = codigo_fornecedor
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.fornecedor_ativo = fornecedor_ativo
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.estado = estado

    def salvar_fornecedor(self):

        conexao = conectar_banco_de_dados_fornecedores()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_FORNECEDORES} (codigo_fornecedor,
        razao_social,
        nome_fantasia,
        fornecedor_ativo,
        cnpj,
        inscricao_estadual,
        logradouro,
        bairro,
        cidade,
        cep,
        estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, 
            (
                self.codigo_fornecedor,
                self.razao_social,
                self.nome_fantasia,
                self.fornecedor_ativo,
                self.cnpj,
                self.inscricao_estadual,
                self.logradouro,
                self.bairro,
                self.cidade,
                self.cep,
                self.estado
            )
        )

        conexao.commit()
        conexao.close()

    def atualizar_fornecedor(self):

        conexao = conectar_banco_de_dados_fornecedores()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        UPDATE {TABELA_FORNECEDORES}
        SET razao_social = ?,
        nome_fantasia = ?,
        fornecedor_ativo = ?,
        cnpj = ?,
        inscricao_estadual = ?,
        logradouro = ?,
        bairro = ?,
        cidade = ?,
        cep = ?,
        estado = ?
        WHERE codigo_fornecedor = ?
        """,
            (
                self.razao_social,
                self.nome_fantasia,
                self.fornecedor_ativo,
                self.cnpj,
                self.inscricao_estadual,
                self.logradouro,
                self.bairro,
                self.cidade,
                self.cep,
                self.estado,
                self.codigo_fornecedor
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_fornecedor(codigo_fornecedor):
        conexao = conectar_banco_de_dados_fornecedores()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_FORNECEDORES}
        WHERE codigo_fornecedor = ?
        """, (codigo_fornecedor,)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_fornecedor_pelo_codigo(codigo_fornecedor):
        try:
            conexao = conectar_banco_de_dados_fornecedores()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            SELECT * FROM {TABELA_FORNECEDORES}
            WHERE codigo_fornecedor = ?
            """, (codigo_fornecedor,)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return Fornecedor(*resultado)
        
        except TypeError:
            return False
        
    @staticmethod
    def buscar_fornecedor_pelo_cnpj(cnpj_fornecedor):
        try:
            conexao = conectar_banco_de_dados_fornecedores()
            cursor = conexao.cursor()

            cursor.execute(
            f"""
            SELECT * FROM {TABELA_FORNECEDORES}
            WHERE cnpj = ?
            """, (cnpj_fornecedor,)
            )

            resultado = cursor.fetchone()

            conexao.commit()
            conexao.close()

            return Fornecedor(*resultado)
        
        except TypeError:
            return False