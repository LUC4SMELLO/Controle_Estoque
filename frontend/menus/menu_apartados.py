import tkinter as tk

from backend.menu_controlador import organizar_botoes

import frontend.menu_state as state


def criar_botao_apartados(janela_pai):
    
    botao_apartados = tk.Button(janela_pai, text="Apartados", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("apartados"))
    botao_apartados.place(x=10, y=110)

    botao_apartar = tk.Button(janela_pai, text="Apartar", width=8, font=("Arial", 10, "bold"))
    botao_historico_apartados = tk.Button(janela_pai, text="Histórico", width=8, font=("Arial", 10, "bold"))

    state.botoes_principais["apartados"] = botao_apartados
    state.botoes_submenus["apartados"] = [botao_apartar, botao_historico_apartados]
