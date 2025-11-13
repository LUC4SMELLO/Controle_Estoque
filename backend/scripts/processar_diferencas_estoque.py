import pandas as pd

def processar_diferencas():
    
    contagem = pd.read_csv("arquivos/contagem_estoque.csv")

    contagem.rename(columns={"codigo": "codigo_produto",
                            "quantidade": "quantidade_contada"}, inplace=True)

    contagem["quantidade_contada"] = pd.to_numeric(
        contagem["quantidade_contada"], errors="coerce"
    )
    contagem["quantidade_contada"] = contagem["quantidade_contada"].fillna(0).astype(int)
    contagem["quantidade_contada"] = contagem["quantidade_contada"].round()


    sistema = pd.read_csv(
        "arquivos/PRODUTOS.CSV",
        header=0,
        delimiter=";",
        encoding="ISO-8859-1",
        index_col=False,
    )

    sistema.rename(
        columns={
            "Codigo": "codigo_produto",
            "Saldo Atual": "quantidade_sistema",
            "DescriÃ§Ã£o": "descricao",
        },
        inplace=True,
    )

    sistema.drop(
        columns=[
            "Cod. CIA",
            "Complemento",
            "UN",
            "Grupo",
            "Categoria",
            "Marca",
            "Custo G",
            "Custo C",
            "Custo UE",
            "Data UE",
            "Fat.GN",
            "Peso Bruto",
            "Peso LÃ­quido",
            "Vol Embalagem",
            "Qtda por Pallet",
            "Qtda por Lastro",
            "Grp Carg",
            "Seq Grp Carg",
            "Cx/Emb",
            "Pos Item",
            "Rest Gaiola",
            "Qnt Emb",
            "Qnt Chapatex",
            "SituaÃ§Ã£o",
            "Descicao Fiscal",
        ],
        inplace=True,
    )

    sistema["quantidade_sistema"] = pd.to_numeric(
        sistema["quantidade_sistema"], errors="coerce"
    )
    sistema["quantidade_sistema"] = sistema["quantidade_sistema"].fillna(0).astype(int)
    sistema["quantidade_sistema"] = sistema["quantidade_sistema"].round()


    comparacao = pd.merge(contagem, sistema, on="codigo_produto", how="outer")

    comparacao["diferenca"] = comparacao["quantidade_contada"] - comparacao["quantidade_sistema"]

    comparacao["status"] = comparacao.apply(
        lambda row: (
            "Estoque Ok"
            if row["diferenca"] == 0
            else "Faltando No Estoque" if row["diferenca"] < 0 else "Sobrando No Estoque"
        ),
        axis=1,
    )

    comparacao = comparacao[
        [
            "codigo_produto",
            "descricao",
            "quantidade_contada",
            "quantidade_sistema",
            "diferenca",
            "status",
        ]
    ]

    return comparacao
