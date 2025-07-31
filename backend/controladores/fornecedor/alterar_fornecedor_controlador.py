from backend.models.fornecedor import Fornecedor

def alterar_fornecedor_back(
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
    fornecedor_atualizado = Fornecedor(
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
    
    fornecedor_atualizado.atualizar_fornecedor()

