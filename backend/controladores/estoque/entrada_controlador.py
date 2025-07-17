import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def entrada_produto_back(codigo_produto: tk.Entry, quantidade_entrada: tk.Entry | int):
    produto = Produto.buscar_produto(codigo_produto.get().strip())
    produto.entrada_estoque_produto(int(quantidade_entrada.get().strip()))

    messagebox.showinfo("Sucesso!", "Entrada Concluída.")
    codigo_produto.focus_set()