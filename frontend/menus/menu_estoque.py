import tkinter as tk

from frontend.janela import janela

from backend.menu_controller import organizar_botoes

import frontend.menu_state as state

def criar_botao_estoque(janela_pai):

    botao_estoque = tk.Button(janela_pai, text="Estoque", font=("Arial", 15, "bold"), command=lambda: organizar_botoes("estoque"))
    botao_estoque.place(x=10, y=60)

    botao_entrada_nota_fiscal = tk.Button(janela_pai, text="Entrada Nota Fiscal")
    botao_entrada_estoque = tk.Button(janela_pai, text="Entrada")
    botao_saida = tk.Button(janela_pai, text="Saída")

    state.botoes_principais["estoque"] = botao_estoque
    state.botoes_submenus["estoque"] = [botao_entrada_nota_fiscal, botao_entrada_estoque, botao_saida]