import tkinter as tk

from frontend.janela import janela

from frontend.menus.menu_produto import criar_botao_produtos
from frontend.menus.menu_estoque import criar_botao_estoque
from frontend.menus.menu_apartados import criar_botao_apartados
from frontend.menus.menu_pendencias import criar_botao_pendencias
from frontend.menus.menu_inventario import criar_botao_inventario
from frontend.menus.menu_fornecedores import criar_botao_fornecedores


def inicializar_interface():
    criar_botao_produtos(janela)
    criar_botao_estoque(janela)
    criar_botao_apartados(janela)
    criar_botao_pendencias(janela)
    criar_botao_inventario(janela)
    criar_botao_fornecedores(janela)

    linha_vertical = tk.Frame(janela, width=6, height=1080, background="silver")
    linha_vertical.place(x=185, y=0)


    janela.mainloop()
