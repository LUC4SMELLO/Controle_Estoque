import tkinter as tk

from frontend.janela import janela

from frontend.menus.menu_produto import criar_botao_produtos
from frontend.menus.menu_estoque import criar_botao_estoque
from frontend.menus.menu_apartados import criar_botao_apartados
from frontend.menus.menu_pendencias import criar_botao_pendencias
from frontend.menus.menu_movimentações import criar_botao_movimentacoes
from frontend.menus.menu_relatorios import criar_botao_relatorios
from frontend.menus.menu_inventario import criar_botao_inventario
from frontend.menus.menu_fornecedores import criar_botao_fornecedores
from frontend.menus.menu_notificacoes import criar_botao_notificacoes
from frontend.menus.menu_validades import criar_botao_validades


def inicializar_interface():
    criar_botao_produtos(janela)
    criar_botao_estoque(janela)
    criar_botao_apartados(janela)
    criar_botao_pendencias(janela)
    criar_botao_movimentacoes(janela)
    criar_botao_relatorios(janela)
    criar_botao_inventario(janela)
    criar_botao_fornecedores(janela)
    criar_botao_notificacoes(janela)
    criar_botao_validades(janela)


    janela.mainloop()
