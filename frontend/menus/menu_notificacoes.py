import tkinter as tk

from backend.controladores.menu.menu_controlador import organizar_botoes

import frontend.menu_state as state

def criar_botao_notificacoes(janela_pai):

    botao_notificacoes = tk.Button(janela_pai, text="Notificações", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("notificacoes"))
    botao_notificacoes.place(x=10, y=410)

    botao_estoque_baixo_notificacoes = tk.Button(janela_pai, text="Estoque Baixo", width=12, font=("Arial", 10, "bold"))
    botao_estoque_inativo_notificacoes = tk.Button(janela_pai, text="Estoque Inativo", width=12, font=("Arial", 10, "bold"))
    botao_data_validade_notificacoes = tk.Button(janela_pai, text="Data Validade", width=12, font=("Arial", 10, "bold"))

    state.botoes_principais["notificacoes"] = botao_notificacoes
    state.botoes_submenus["notificacoes"] = [botao_estoque_baixo_notificacoes, botao_estoque_inativo_notificacoes, botao_data_validade_notificacoes]
