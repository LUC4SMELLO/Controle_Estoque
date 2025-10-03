import tkinter as tk

from backend.controladores.menu.menu_controlador import organizar_botoes

from frontend.janelas.inventario.janela_contagem_produtos import criar_janela_contagem_produtos

import frontend.menu_state as state

def criar_botao_inventario(janela_pai):

    botao_inventario = tk.Button(janela_pai, text="Inventário", font=("Arial", 15, "bold"), width=13, command=lambda: organizar_botoes("inventario"))
    botao_inventario.place(x=10, y=310)

    botao_contagem_produtos_inventario = tk.Button(janela_pai, text="Contagem Produtos", width=16, font=("Arial", 10, "bold"), command=criar_janela_contagem_produtos)
    botao_contagem_doces_inventario = tk.Button(janela_pai, text="Contagem Doces", width=15, font=("Arial", 10, "bold"))
    botao_ajustar_diferencas_inventario = tk.Button(janela_pai, text="Ajustar Diferenças", width=15, font=("Arial", 10, "bold"))
    botao_comparar_estoque_inventario = tk.Button(janela_pai, text="Comparar Estoque", width=15, font=("Arial", 10, "bold"))

    state.botoes_principais["inventario"] = botao_inventario
    state.botoes_submenus["inventario"] = [botao_contagem_produtos_inventario, botao_contagem_doces_inventario, botao_ajustar_diferencas_inventario, botao_comparar_estoque_inventario,]
