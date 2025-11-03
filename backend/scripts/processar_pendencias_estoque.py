import pandas as pd

def processar_pendencias():

    dados = pd.read_excel(
        "arquivos/CONTROLE OPERACIONAL  - OUT25.xlsm",
        sheet_name="Estoque1",
        header=4,
        usecols=['Cupom', 'CLIENTE', 'DT.OC.', 'RAZÃO SOCIAL', 'CIDADE', 'DIA',
        'VENDEDOR', 'PROD 1', 'QUANT 1', 'PROD 2', 'QUANT 2', 'PROD 3',
        'QUANT 3', 'PROD 4', 'QUANT 4', 'PROD 5', 'QUANT 5', 'PROD 6',
        'QUANT 6', 'Cup.Orig', 'STATUS'])


    pendencias = dados[(dados['STATUS'] == 'ENTREGA PENDENTE') & (dados['Cup.Orig'] == 'P')]

    return pendencias
