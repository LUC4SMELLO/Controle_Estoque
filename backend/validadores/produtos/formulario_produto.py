def validar_formulario_produto(
        codigo_produto,
        descricao,
        subdescricao,
        unidade_medida,
        itens_embalagem,
        codigo_barras,
        grupo,
        categoria,
        marca,
        itens_pallete,
        itens_lastro,
    ):

    if not codigo_produto or not descricao or not subdescricao or not unidade_medida or not itens_embalagem or not codigo_barras or not grupo or not categoria or not marca or not itens_pallete or not itens_lastro:
        return False, "Todos os Campos Devem ser Preechidos."
    
    if len(codigo_barras) != 13:
        return False, "Código de Barras Inválido."

    return True, "Cadastro Válido."