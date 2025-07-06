import tkinter as tk
from frontend.janela import janela

import frontend.menus.menu_produtos as menu_produtos

botao_nota_fiscal_estoque = tk.Button(janela, text="Nota Fiscal", font=("Arial", 10, "bold"))
botao_entrada_estoque = tk.Button(janela, text="Entrada", font=("Arial", 10, "bold"))
botao_saida_estoque = tk.Button(janela, text="Saída", font=("Arial", 10, "bold"))

botoes_sendo_mostrados_estoque = False
espacamento = 90

def mostrar_botoes_estoque(botao_apartados):

    global botoes_sendo_mostrados_estoque


    if menu_produtos.botoes_sendo_mostrados_produtos and botoes_sendo_mostrados_estoque:
        botao_nota_fiscal_estoque.place_forget()
        botao_entrada_estoque.place_forget()
        botao_saida_estoque.place_forget()

        botoes_sendo_mostrados_estoque = False

        botao_apartados.place(x=10, y=200)
        return
    
    if botoes_sendo_mostrados_estoque:
        botao_nota_fiscal_estoque.place_forget()
        botao_entrada_estoque.place_forget()
        botao_saida_estoque.place_forget()

        botoes_sendo_mostrados_estoque = False

        botao_apartados.place(x=10, y=110)
        return
    
    if menu_produtos.botoes_sendo_mostrados_produtos:
        botao_nota_fiscal_estoque.place(x=50, y=105 + 90)
        botao_entrada_estoque.place(x=50, y=135 + 90)
        botao_saida_estoque.place(x=50, y=165 + 90)

        botoes_sendo_mostrados_estoque = True

        botao_apartados.place(x=10, y=290)
        return
    
    

    
    if botoes_sendo_mostrados_estoque == False:
        botao_nota_fiscal_estoque.place(x=50, y=105)
        botao_entrada_estoque.place(x=50, y=135)
        botao_saida_estoque.place(x=50, y=165)

        botoes_sendo_mostrados_estoque = True

        botao_apartados.place(x=10, y=200)
        return