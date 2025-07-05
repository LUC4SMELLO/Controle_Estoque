import tkinter as tk

from frontend.janela import janela

from frontend.menus.menu_produtos import mostrar_botoes_produtos
from frontend.menus.menu_estoque import mostrar_botoes_estoque
        
def mostrar_frame(frame):
    frame.place(x=100, y=10)

def inicializar_interface():

    botao_produtos = tk.Button(janela, text="Produtos", font=("Arial", 15, "bold"), command=lambda: mostrar_botoes_produtos(botao_estoque, botao_apartados))
    botao_produtos.place(x=10, y=10)

    botao_estoque = tk.Button(janela, text="Estoque", font=("Arial", 15, "bold"), width=8,command=lambda: mostrar_botoes_estoque(botao_apartados))
    botao_estoque.place(x=10, y=60)
    
    botao_apartados = tk.Button(janela, text="Apartados", font=("Arial", 15, "bold"))
    botao_apartados.place(x=10, y=110)



    janela.mainloop()