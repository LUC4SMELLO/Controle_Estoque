import pandas as pd

def processar_pendencias():

    dados = pd.read_excel(
        "arquivos/CONTROLE OPERACIONAL  - OUT25.xlsm",
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

    return pendencias
