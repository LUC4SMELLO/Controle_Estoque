import pandas as pd

from database.banco_dados_pendencias import conectar_banco_de_dados_pendencias

from backend.constantes.bancos_dados import TABELA_PENDENCIAS

def processar_pendencias():

    dados = pd.read_excel(
        "arquivos/CONTROLE OPERACIONAL  - NOV25.xlsm",
        sheet_name="Estoque1",
        header=4,
        usecols=['Cupom', 'DT.OC.', 'CLIENTE', 'RAZÃO SOCIAL', 'CIDADE',
        'VENDEDOR', 'PROD 1', 'QUANT 1', 'Cup.Orig', 'STATUS'])
        
    dados["Cupom"] = dados["Cupom"].astype(str)
    dados["DT.OC."] = dados["DT.OC."].astype(str)
    dados["RAZÃO SOCIAL"] = dados["RAZÃO SOCIAL"].astype(str)
    dados["CIDADE"] = dados["CIDADE"].astype(str)
    dados["VENDEDOR"] = dados["VENDEDOR"].astype(str)
    dados["PROD 1"] = dados["PROD 1"].astype(str)
    dados["Cup.Orig"] = dados["Cup.Orig"].astype(str)
    dados["STATUS"] = dados["STATUS"].astype(str)

    dados["QUANT 1"] = pd.to_numeric(dados["QUANT 1"], errors="coerce")
    dados["QUANT 1"] = dados["QUANT 1"].fillna(0).astype(int).abs()


    pendencias = dados[(dados['STATUS'] == 'ENTREGA PENDENTE') & (dados['Cup.Orig'] == 'P')]

    pendencias = pendencias[[
        'Cupom',
        'DT.OC.',
        'CLIENTE',
        'RAZÃO SOCIAL',
        'CIDADE',
        'VENDEDOR',
        'PROD 1',
        'QUANT 1',
        'Cup.Orig',
        'STATUS']]

    conexao = conectar_banco_de_dados_pendencias()
    cursor = conexao.cursor()


    cursor.execute(f"DELETE FROM {TABELA_PENDENCIAS}")


    for i, linha in pendencias.iterrows():
        cursor.execute(
        f"""
        INSERT INTO {TABELA_PENDENCIAS} (
        cupom,
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
                linha["Cupom"],
                linha["DT.OC."],
                linha["CLIENTE"],
                linha["RAZÃO SOCIAL"],
                linha["CIDADE"],
                linha["VENDEDOR"],
                linha["PROD 1"],
                linha["QUANT 1"],
            )
        )

    conexao.commit()
    conexao.close()
