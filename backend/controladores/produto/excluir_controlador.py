
from backend.models.produto import Produto

def excluir_produto_back(codigo_produto):

    Produto.excluir_produto(codigo_produto)
