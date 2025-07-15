import tkinter as tk
from tkinter import messagebox

from backend.models.produto import Produto


def alterar_produto_back(
    codigo_produto: tk.Entry,
    descricao: tk.Entry,
    subdescrica: tk.Entry,
    produto_ativo: tk.BooleanVar,
    unidade_medida: tk.Entry,
    itens_embalagem_produtos: tk.Entry,
    codigo_barras: tk.Entry,
    grupo_produtos: tk.Entry,
    categorias_produtos: tk.Entry,
    marca_produtos: tk.Entry,
    itens_pallete: tk.Entry,
    itens_lastro: tk.Entry,
):

    produto = Produto(
        codigo_produto.get().strip(),
        descricao.get().strip(),
        subdescrica.get().strip(),
        produto_ativo.get(),
        unidade_medida.get().strip(),
        itens_embalagem_produtos.get().strip(),
        codigo_barras.get().strip(),
        grupo_produtos.get().strip(),
        categorias_produtos.get().strip(),
        marca_produtos.get().strip(),
        itens_pallete.get().strip(),
        itens_lastro.get().strip(),
    )
    produto.atualizar_produto()

    messagebox.showinfo("Sucesso!", "Produto Alterado.")
    codigo_produto.focus_set()
