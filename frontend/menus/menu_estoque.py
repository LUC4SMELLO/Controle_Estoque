import tkinter as tk
from frontend.janela import janela

botao_nota_fiscal_estoque = tk.Button(janela, text="Nota Fiscal", font=("Arial", 10, "bold"))
botao_entrada_estoque = tk.Button(janela, text="Entrada", font=("Arial", 10, "bold"))
botao_saida_estoque = tk.Button(janela, text="Saída", font=("Arial", 10, "bold"))

botoes_sendo_mostrados = False
def mostrar_botoes_estoque(botao_apartados):

    global botoes_sendo_mostrados

    if botoes_sendo_mostrados:
        botao_nota_fiscal_estoque.place_forget()
        botao_entrada_estoque.place_forget()
        botao_saida_estoque.place_forget()

        botoes_sendo_mostrados = False

        botao_apartados.place(x=10, y=110)
        

    else:
        botao_nota_fiscal_estoque.place(x=50, y=105)
        botao_entrada_estoque.place(x=50, y=135)
        botao_saida_estoque.place(x=50, y=165)

        botoes_sendo_mostrados = True

        botao_apartados.place(x=10, y=200)
