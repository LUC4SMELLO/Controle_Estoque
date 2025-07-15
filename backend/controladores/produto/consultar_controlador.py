from backend.models.produto import Produto

def buscar_produto_back(codigo: str):
    
    if not codigo.strip():
        return False, "Preencha o Código do Produto."

    resultado = Produto.buscar_produto(codigo.strip())

    if not resultado:
        return False, "Produto Não Encontrado."

    return True, resultado
