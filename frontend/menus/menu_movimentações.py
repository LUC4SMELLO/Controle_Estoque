import tkinter as tk

from backend.menu_controller import organizar_botoes

import frontend.menu_state as state

def criar_botao_movimentacoes(janela_pai):

    botao_movimentacoes = tk.Button(janela_pai, text="Movimentações", font=("Arial", 15, "bold"), command=lambda: organizar_botoes("movimentacoes"))
    botao_movimentacoes.place(x=10, y=210)

    botao_entradas_movimentacoes = tk.Button(janela_pai, text="Entradas", font=("Arial", 10, "bold"))
    botao_saidas_movimentacoes = tk.Button(janela_pai, text="Saídas", font=("Arial", 10, "bold"))
    botao_historico_movimentacoes = tk.Button(janela_pai, text="Histórico", font=("Arial", 10, "bold"))

    state.botoes_principais["movimentacoes"] = botao_movimentacoes
    state.botoes_submenus["movimentacoes"] = [botao_entradas_movimentacoes, botao_saidas_movimentacoes, botao_historico_movimentacoes]
