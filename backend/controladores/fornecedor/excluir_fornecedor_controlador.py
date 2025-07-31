from backend.models.fornecedor import Fornecedor

def excluir_fornecedor_back(codigo_fornecedor: str):

    Fornecedor.excluir_fornecedor(codigo_fornecedor)

    