import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controladores.estoque.saida_controlador import saida_produto_back

from backend.binds.configuracao_binds import configurar_binds 

def criar_janela_saida_produtos():

    def saida_produto_gui():
        
        codigo_produto = entry_codigo_produto_saida
        quantidade = entry_quantidade_saida

        saida_produto_back(codigo_produto, quantidade)

    janela_saida_produtos = tk.Toplevel()
    janela_saida_produtos.title("Saída Produto")
    janela_saida_produtos.geometry("400x300")


    label_data_saida = tk.Label(janela_saida_produtos, text="Data Saída:", font=("Arial", 10, "bold"))
    label_data_saida.place(x=38, y=10)

    entry_data_saida = tk.Entry(janela_saida_produtos, width=10, font=("Arial", 10, "bold"))
    entry_data_saida.place(x=120, y=10)

    label_codigo_produto = tk.Label(janela_saida_produtos, text="Código Produto:", font=("Arial", 10, "bold"))
    label_codigo_produto.place(x=10, y=50)

    entry_codigo_produto_saida = tk.Entry(janela_saida_produtos, width=10, font=("Arial", 10, "bold"))
    entry_codigo_produto_saida.place(x=120, y=50)

    label_quantidade_saida = tk.Label(janela_saida_produtos, text="Quantidade:", font=("Arial", 10, "bold"))
    label_quantidade_saida.place(x=34, y=90)

    entry_quantidade_saida = tk.Entry(janela_saida_produtos, width=10, font=("Arial", 10, "bold"))
    entry_quantidade_saida.place(x=120, y=90)

    label_motivo_saida = tk.Label(janela_saida_produtos, text="Motivo:", font=("Arial", 10, "bold"))
    label_motivo_saida.place(x=66, y=150)

    entry_motivo_saida = tk.Text(janela_saida_produtos, width=35, height=3, font=("Arial", 10, "bold"))
    entry_motivo_saida.place(x=120, y=150)

    linha_horizontal_inferior = tk.Frame(janela_saida_produtos,  background="silver", width=500, height=5)
    linha_horizontal_inferior.place(x=0, y=250)

    botao_confirmar_saida = tk.Button(janela_saida_produtos, text="Confirmar", font=("Arial", 10, "bold"), command=saida_produto_gui)
    botao_confirmar_saida.place(x=200, y=265)

    botao_cancelar_saida = tk.Button(janela_saida_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_saida.place(x=300, y=265)


    lista_entrys = [entry_data_saida,
                    entry_codigo_produto_saida,
                    entry_quantidade_saida,
                    entry_motivo_saida,
                    botao_confirmar_saida
                    ]
    
    acoes_intermediarias = [None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, saida_produto_gui)