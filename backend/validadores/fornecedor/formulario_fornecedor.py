def validar_formulario_fornecedor(
        codigo_fornecedor,
        razao_social,
        nome_fantasia,
        cnpj,
        inscricao_estadual,
        logradouro,
        bairro,
        cidade,
        cep,
        estado
    ):

    if not codigo_fornecedor or not razao_social or not \
    nome_fantasia or not cnpj or not \
    inscricao_estadual or not logradouro or not \
    bairro or not cidade or not cep or not estado:
        return False, "Todos os Campos Devem ser Preenchidos."
    
    if len(cnpj) != 14:
        return False, "CNPJ Inválido."    
    
    if len(inscricao_estadual) != 13:
        return False, "Inscrição Estadual Inválida."
    
    return True, "Cadastro Válido."
