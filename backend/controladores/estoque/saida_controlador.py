import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def saida_produto_back(codigo_produto: str, quantidade_entrada: int):
    produto = Produto.buscar_produto(codigo_produto.get().strip())
    produto.saida_estoque_produto(int(quantidade_entrada.get().strip()))
