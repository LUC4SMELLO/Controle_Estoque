import sqlite3
import pandas as pd

from database.banco_dados_produtos import conectar_banco_de_dados_produtos

from backend.constantes.bancos_dados import TABELA_PRODUTOS


def processar_estoque_sistema(caminho_arquivo):

    if not caminho_arquivo:
        return False, "Arquivo vazio ou não encontrado."

    try:
        arquivo_parametro = pd.read_csv(
        caminho_arquivo,
        header=0,
        delimiter=";",
        encoding="ISO-8859-1",
        index_col=False,
        usecols=(["Codigo", "Cod. CIA", "DescriÃ§Ã£o", "Saldo Atual", "Grupo"])
        )

        arquivo_parametro.rename(columns={"DescriÃ§Ã£o": "Descricao"}, inplace=True)

        arquivo_parametro["Codigo"] = arquivo_parametro["Codigo"].astype(str)
        arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].astype(str)
        arquivo_parametro["Descricao"] = arquivo_parametro["Descricao"].astype(str)

        arquivo_parametro["Saldo Atual"] = pd.to_numeric(arquivo_parametro["Saldo Atual"], errors="coerce")
        arquivo_parametro["Saldo Atual"] = arquivo_parametro["Saldo Atual"].fillna(0).astype(int)

        arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].str.lstrip("0")


        # ESTE TRECHO EXCLUI DETERMINADOS GRUPOS DE PRODUTOS
        arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != "099-MATERIAL                  "]
        arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != "013-BALAS E GOMAS             "]
        arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != "020-ALIMENTOS                 "]
        arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != "019-SNACKS                    "]

        # ESTE TRECHO FILTRA O GÁS CERTO
        arquivo_parametro = arquivo_parametro[
            (arquivo_parametro["Grupo"] != "023-GAS CO2                   ") |
            ((arquivo_parametro["Grupo"] == "023-GAS CO2                   ") &
            (arquivo_parametro["Codigo"].isin(["120120", "120121"])))
        ]

        arquivo_parametro.drop(columns=["Grupo"], inplace=True)

        return arquivo_parametro, "Sucesso!, processamento concluído."

    except Exception as erro:
        return False, f"Ocorreu um erro: {erro}"
    

def atualizar_estoque_produto(arquivo_parametro) -> bool:
    try:
        conexao = conectar_banco_de_dados_produtos()
        cursor = conexao.cursor()

        for i, linha in arquivo_parametro.iterrows():

            cursor.execute(
            f"""
            UPDATE {TABELA_PRODUTOS}
            SET quantidade_estoque = ?
            WHERE codigo_produto = ?
            """,
                (
                    linha["Saldo Atual"],
                    linha["Codigo"]
                )
            )

        conexao.commit()
        conexao.close()

        return True, "Sucesso!, produtos atualizados."
    
    except Exception as erro:
        return False, f"Ocorreu um erro: {erro}"







    

def processar_estoque_contado():
    pass
