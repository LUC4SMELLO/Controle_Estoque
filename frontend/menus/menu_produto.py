import tkinter as tk

from frontend.janela import janela

from backend.menu_controller import organizar_botoes

import frontend.menu_state as state

def criar_botao_produtos(janela_pai):
    botao_produtos = tk.Button(janela_pai, text="Produtos", font=("Arial", 15, "bold"), command=lambda: organizar_botoes("produtos"))
    botao_produtos.place(x=10, y=10)

    botao_cadastrar_produto = tk.Button(janela_pai, text="Cadastrar")
    botao_alterar_produto = tk.Button(janela_pai, text="Alterar")
    botao_excluir_produto = tk.Button(janela_pai, text="Excluir")

    state.botoes_principais["produtos"] = botao_produtos
    state.botoes_submenus["produtos"] = [botao_cadastrar_produto, botao_alterar_produto, botao_excluir_produto]