import tkinter as tk

from backend.controladores.menu.menu_controlador import organizar_botoes

from frontend.janelas.pendencias.janela_historico_pendencias import criar_janela_historico_pendencias

import frontend.menu_state as state

def criar_botao_pendencias(janela_pai):

    botao_pendencias = tk.Button(janela_pai, text="Pendências", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("pendencias"))
    botao_pendencias.place(x=10, y=160)

    botao_historico_pendencia = tk.Button(janela_pai, text="Histórico", width=8, font=("Arial", 10, "bold"), command=criar_janela_historico_pendencias)

    state.botoes_principais["pendencias"] = botao_pendencias
    state.botoes_submenus["pendencias"] = [botao_historico_pendencia]


    
