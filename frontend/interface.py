import tkinter as tk

from frontend.janela import janela

from frontend.menus.menu_produtos import mostrar_botoes_produtos
        
def mostrar_frame(frame):
    frame.place(x=100, y=10)

def inicializar_interface():

    botao_produtos = tk.Button(janela, text="Produtos", font=("Arial", 15, "bold"), command=lambda: mostrar_botoes_produtos(botao_estoque))
    botao_produtos.place(x=10, y=10)

    botao_estoque = tk.Button(janela, text="Estoque", font=("Arial", 15, "bold"), width=8)
    botao_estoque.place(x=10, y=60)
    



    janela.mainloop()