import tkinter as tk
from tkinter import messagebox, ttk

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

produtos = [
    {"codigo": 8533, "nome": "Coca Cola Lata 350ml", "quantidade": 0},
    {"codigo": 9334, "nome": "Coca Cola Zero Lata 350ml", "quantidade": 0},
    {"codigo": 9335, "nome": "Guaraná Antarctica Lata 350ml", "quantidade": 0},
    {"codigo": 9336, "nome": "Guaraná Antarctica Zero Lata 350ml", "quantidade": 0},
    {"codigo": 9337, "nome": "Fanta Laranja Lata 350ml", "quantidade": 0},
    {"codigo": 9338, "nome": "Fanta Uva Lata 350ml", "quantidade": 0},
    {"codigo": 9339, "nome": "Sprite Lata 350ml", "quantidade": 0},
    {"codigo": 9340, "nome": "Água Mineral Sem Gás 500ml", "quantidade": 0},
    {"codigo": 9341, "nome": "Água Mineral Com Gás 500ml", "quantidade": 0},
    {"codigo": 9342, "nome": "Cerveja Pilsen Lata 350ml", "quantidade": 0},
    {"codigo": 9343, "nome": "Cerveja Puro Malte Lata 350ml", "quantidade": 0},
    {"codigo": 9344, "nome": "Salgadinho Batata Original 100g", "quantidade": 0}
    ]

def criar_janela_contagem_produtos():

    janela_contagem_produtos = tk.Toplevel()
    janela_contagem_produtos.title("Contagem Produtos")
    janela_contagem_produtos.geometry("1920x1080")

    janela_contagem_produtos.state("zoomed")


    x = 10
    y = 10

    for produto in produtos:

        codigo_produto = tk.Label(janela_contagem_produtos, text=produto["codigo"], font=LABEL)
        codigo_produto.place(x=x, y=y)

        nome_produto = tk.Label(janela_contagem_produtos, text=produto["nome"], font=LABEL)
        nome_produto.place(x=x+50, y=y)

        quantidade_produto = tk.Label(janela_contagem_produtos, text=produto["quantidade"], font=LABEL)
        quantidade_produto.place(x=x+300, y=y)

        y += 27


    