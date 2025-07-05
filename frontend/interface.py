import tkinter as tk

from frontend.janela import janela

from frontend.menus.produtos_menus import mostrar_botoes_produtos
        
def mostrar_frame(frame):
    frame.place(x=100, y=10)

def inicializar_interface():

    botao_produtos = tk.Button(janela, text="Produtos", font=("Arial", 15, "bold"), command=mostrar_botoes_produtos)
    botao_produtos.place(x=10, y=10)

    



    janela.mainloop()