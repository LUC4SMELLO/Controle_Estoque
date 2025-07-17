import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.binds.configuracao_binds import configurar_binds 

def criar_janela_entrada_produtos():

    def entrada_produto_gui():
        pass

    janela_entrada_produtos = tk.Toplevel()
    janela_entrada_produtos.title("Entrada Produto")
    janela_entrada_produtos.geometry("500x300")


    label_data_entrada = tk.Label(janela_entrada_produtos, text="Data Entrada:", font=("Arial", 10, "bold"))
    label_data_entrada.place(x=26, y=10)

    entry_data_entrada = tk.Entry(janela_entrada_produtos, width=10, font=("Arial", 10, "bold"))
    entry_data_entrada.place(x=120, y=10)

    label_codigo_produto = tk.Label(janela_entrada_produtos, text="Código Produto:", font=("Arial", 10, "bold"))
    label_codigo_produto.place(x=10, y=50)

    entry_codigo_produto_entrada = tk.Entry(janela_entrada_produtos, width=10, font=("Arial", 10, "bold"))
    entry_codigo_produto_entrada.place(x=120, y=50)

    label_quantidade_entrada = tk.Label(janela_entrada_produtos, text="Quantidade:", font=("Arial", 10, "bold"))
    label_quantidade_entrada.place(x=34, y=90)

    entry_quantidade_entrada = tk.Entry(janela_entrada_produtos, width=10, font=("Arial", 10, "bold"))
    entry_quantidade_entrada.place(x=120, y=90)

    label_motivo_entrada = tk.Label(janela_entrada_produtos, text="Motivo:", font=("Arial", 10, "bold"))
    label_motivo_entrada.place(x=66, y=150)

    entry_motivo_entrada = tk.Text(janela_entrada_produtos, width=35, height=3, font=("Arial", 10, "bold"))
    entry_motivo_entrada.place(x=120, y=150)

    linha_horizontal_inferior = tk.Frame(janela_entrada_produtos,  background="silver", width=500, height=5)
    linha_horizontal_inferior.place(x=0, y=250)

    botao_confirmar_entrada = tk.Button(janela_entrada_produtos, text="Confirmar", font=("Arial", 10, "bold"))
    botao_confirmar_entrada.place(x=300, y=265)

    botao_cancelar_entrada = tk.Button(janela_entrada_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_entrada.place(x=400, y=265)


    lista_entrys = [entry_data_entrada,
                    entry_codigo_produto_entrada,
                    entry_quantidade_entrada,
                    entry_motivo_entrada,
                    botao_confirmar_entrada
                    ]
    
    acoes_intermediarias = [None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, entrada_produto_gui)