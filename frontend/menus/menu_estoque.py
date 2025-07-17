import tkinter as tk

from backend.controladores.menu_controlador import organizar_botoes

from frontend.janelas.estoque.entrada import criar_janela_entrada_produtos

import frontend.menu_state as state

def criar_botao_estoque(janela_pai):

    botao_estoque = tk.Button(janela_pai, text="Estoque", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("estoque"))
    botao_estoque.place(x=10, y=60)

    botao_entrada_nota_fiscal = tk.Button(janela_pai, text="Entrada Nota Fiscal", font=("Arial", 10, "bold"))
    botao_entrada_estoque = tk.Button(janela_pai, text="Entrada", width=8, font=("Arial", 10, "bold"), command=criar_janela_entrada_produtos)
    botao_saida_estoque = tk.Button(janela_pai, text="Saída", width=8,  font=("Arial", 10, "bold"))

    state.botoes_principais["estoque"] = botao_estoque
    state.botoes_submenus["estoque"] = [botao_entrada_nota_fiscal, botao_entrada_estoque, botao_saida_estoque]
