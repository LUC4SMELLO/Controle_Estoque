import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def saida_produto_back(codigo_produto: tk.Entry, quantidade_entrada: tk.Entry | int):
    produto = Produto.buscar_produto(codigo_produto.get().strip())
    produto.saida_estoque_produto(int(quantidade_entrada.get().strip()))

    messagebox.showinfo("Sucesso!", "Saída Concluída.")
    codigo_produto.focus_set()