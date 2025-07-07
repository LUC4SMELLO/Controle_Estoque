import tkinter as tk

from backend.menu_controller import organizar_botoes

import frontend.menu_state as state

def criar_botao_inventario(janela_pai):

    botao_inventario = tk.Button(janela_pai, text="Inventário", font=("Arial", 15, "bold"), command=lambda: organizar_botoes("inventario"))
    botao_inventario.place(x=10, y=310)

    botao_digitar_estoque_inventario = tk.Button(janela_pai, text="Digitação", font=("Arial", 10, "bold"))
    botao_comparar_estoque_inventario = tk.Button(janela_pai, text="Comparar Estoque", font=("Arial", 10, "bold"))
    botao_doces_alimentos_inventario = tk.Button(janela_pai, text="Doces Alimentos", font=("Arial", 10, "bold"))

    state.botoes_principais["inventario"] = botao_inventario
    state.botoes_submenus["inventario"] = [botao_digitar_estoque_inventario, botao_doces_alimentos_inventario, botao_comparar_estoque_inventario,]
