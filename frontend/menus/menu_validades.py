import tkinter as tk

from backend.menu_controlador import organizar_botoes

import frontend.menu_state as state

def criar_botao_validades(janela_pai):

    botao_validades = tk.Button(janela_pai, text="Validades", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("validades"))
    botao_validades.place(x=10, y=460)

    botao_cadastrar_validades = tk.Button(janela_pai, text="Cadastrar", width=8, font=("Arial", 10, "bold"))
    botao_alterar_validades = tk.Button(janela_pai, text="Alterar", width=8, font=("Arial", 10, "bold"))
    botao_excluir_validades = tk.Button(janela_pai, text="Excluir", width=8, font=("Arial", 10, "bold"))
    botao_consultar_validades = tk.Button(janela_pai, text="Consultar", width=8, font=("Arial", 10, "bold"))

    state.botoes_principais["validades"] = botao_validades
    state.botoes_submenus["validades"] = [botao_cadastrar_validades, botao_alterar_validades, botao_excluir_validades, botao_consultar_validades]

