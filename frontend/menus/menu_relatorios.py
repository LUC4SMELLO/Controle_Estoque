import tkinter as tk

from backend.menu_controlador import organizar_botoes

import frontend.menu_state as state

def criar_botao_relatorios(janela_pai):

    botao_relatorios = tk.Button(janela_pai, text="Relatórios", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("relatorios"))
    botao_relatorios.place(x=10, y=260)

    botao_produtos_relatorios = tk.Button(janela_pai, text="Produtos", width=8, font=("Arial", 10, "bold"))
    botao_entradas_saidas_relatorios = tk.Button(janela_pai, text="Entradas e Saídas", font=("Arial", 10, "bold"))
    botao_validade_relatorios = tk.Button(janela_pai, text="Validade", width=8, font=("Arial", 10, "bold"))
    botao_lotes_relatorios = tk.Button(janela_pai, text="Lotes", width=8, font=("Arial", 10, "bold"))


    state.botoes_principais["relatorios"] = botao_relatorios
    state.botoes_submenus["relatorios"] = [botao_produtos_relatorios, botao_entradas_saidas_relatorios, botao_validade_relatorios, botao_lotes_relatorios]