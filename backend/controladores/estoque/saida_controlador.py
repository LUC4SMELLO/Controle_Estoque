import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def saida_produto_back(codigo_produto: str, quantidade_entrada: int):
    """
    Da saída na quantidade em estoque de algum produto no banco de dados.

    Parameters
    ----------
        codigo_produto
            O código do produto.
            
        quantidade_entrada
            O valor da quantidade que vai sair.
            
    Returns
    -------
        None
        
    """
    
    produto = Produto.buscar_produto_por_codigo(codigo_produto.get().strip())
    produto.saida_estoque_produto(int(quantidade_entrada.get().strip()))
