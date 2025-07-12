import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto

def excluir_produto_back(codigo_produto: tk.Entry):

    Produto.excluir_produto(codigo_produto.get().strip())

    messagebox.showinfo("Sucesso!", "Produto Excluído.")

    codigo_produto.focus_set()

def limpar_entradas_excluir_produto(entradas: list):

    for entrada in entradas:
        entrada.delete(0, tk.END)