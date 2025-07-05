import tkinter as tk
from frontend.janela import janela




botao_cadastrar_produto = tk.Button(janela, text="Cadastrar", font=("Arial", 10, "bold"))
botao_alterar_produto = tk.Button(janela, text="Alterar", font=("Arial", 10, "bold"))
botao_excluir_produto = tk.Button(janela, text="Excluir", font=("Arial", 10, "bold"))   




botoes_sendo_mostrados = False

def mostrar_botoes_produtos(botao_estoque):
    global botoes_sendo_mostrados

    if botoes_sendo_mostrados:
        botao_cadastrar_produto.place_forget()
        botao_alterar_produto.place_forget()
        botao_excluir_produto.place_forget()
        botoes_sendo_mostrados = False

        botao_estoque.place(x=10, y=60)

    else:
        botao_cadastrar_produto.place(x=50, y=55)
        botao_alterar_produto.place(x=50, y=85)
        botao_excluir_produto.place(x=50, y=115)
        botoes_sendo_mostrados = True

        botao_estoque.place(x=10, y=150)
        
