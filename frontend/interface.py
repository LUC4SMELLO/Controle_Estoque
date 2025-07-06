import tkinter as tk

from frontend.janela import janela

from frontend.menus.menu_produto import criar_botao_produtos
from frontend.menus.menu_estoque import criar_botao_estoque
from frontend.menus.menu_apartados import criar_botao_apartados


def mostrar_frame(frame):
    frame.place(x=100, y=10)

def inicializar_interface():
    criar_botao_produtos(janela)
    criar_botao_estoque(janela)
    criar_botao_apartados(janela)



    janela.mainloop()