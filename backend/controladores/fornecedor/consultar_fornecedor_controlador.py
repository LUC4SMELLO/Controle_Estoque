from backend.models.fornecedor import Fornecedor

def buscar_fornecedor_back(codigo: str):
    
    if not codigo.strip():
        return False, "Preencha o Código do Fornecedor."

    resultado = Fornecedor.buscar_fornecedor_pelo_codigo(codigo.strip())

    if not resultado:
        return False, "Fornecedor Não Encontrado."

    return True, resultado
