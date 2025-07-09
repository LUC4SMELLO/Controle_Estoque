import tkinter as tk

from backend.menu_controller import organizar_botoes

from frontend.janelas.produtos.cadastrar_produto import criar_janela_cadastrar_produto
from frontend.janelas.produtos.alterar_produto import criar_janela_alterar_produto

import frontend.menu_state as state

def criar_botao_produtos(janela_pai):

    botao_produtos = tk.Button(janela_pai, text="Produtos", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("produtos"))
    botao_produtos.place(x=10, y=10)

    botao_cadastrar_produto = tk.Button(janela_pai, text="Cadastrar", font=("Arial", 10, "bold"), command=criar_janela_cadastrar_produto)
    botao_alterar_produto = tk.Button(janela_pai, text="Alterar", width=8, font=("Arial", 10, "bold"), command=criar_janela_alterar_produto)
    botao_excluir_produto = tk.Button(janela_pai, text="Excluir", width=8, font=("Arial", 10, "bold"))
    botao_consultar_produto = tk.Button(janela_pai, text="Consultar", width=8, font=("Arial", 10, "bold"))

    state.botoes_principais["produtos"] = botao_produtos
    state.botoes_submenus["produtos"] = [botao_cadastrar_produto, botao_alterar_produto, botao_excluir_produto, botao_consultar_produto]
    