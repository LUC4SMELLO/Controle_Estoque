from backend.models.fornecedor import Fornecedor


def cadastrar_fornecedor_back(
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
        estado
    ):

    novo_fornecedor = Fornecedor(
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
        estado
    )

    novo_fornecedor.salvar_fornecedor()
