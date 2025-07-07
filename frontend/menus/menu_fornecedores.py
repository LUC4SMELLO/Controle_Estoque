import tkinter as tk

from backend.menu_controller import organizar_botoes

import frontend.menu_state as state

def criar_botao_fornecedores(janela_pai):

    botao_fornecedores = tk.Button(janela_pai, text="Fornecedores", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("fornecedores"))
    botao_fornecedores.place(x=10, y=360)

    botao_cadastrar_fornecedores = tk.Button(janela_pai, text="Cadastrar", font=("Arial", 10, "bold"))
    botao_alterar_fornecedores = tk.Button(janela_pai, text="Alterar", font=("Arial", 10, "bold"))
    botao_excluir_fornecedores = tk.Button(janela_pai, text="Excluir", font=("Arial", 10, "bold"))
    botao_consultar_fornecedores = tk.Button(janela_pai, text="Consultar", font=("Arial", 10, "bold"))

    botao_ultimas_compras = tk.Button(janela_pai, text="Últimas Compras", font=("Arial", 10, "bold"))

    state.botoes_principais["fornecedores"] = botao_fornecedores
    state.botoes_submenus["fornecedores"] = [
        botao_cadastrar_fornecedores,
        botao_alterar_fornecedores,
        botao_excluir_fornecedores,
        botao_consultar_fornecedores,
        botao_ultimas_compras
    ]
