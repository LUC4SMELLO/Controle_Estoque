import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def entrada_produto_back(codigo_produto: str, quantidade_entrada: int):
    produto = Produto.buscar_produto_por_codigo(codigo_produto)
    produto.entrada_estoque_produto(int(quantidade_entrada))
