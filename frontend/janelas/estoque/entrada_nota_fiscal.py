import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.controladores.estoque.entrada_controlador import entrada_produto_back

from backend.binds.configuracao_binds import configurar_binds 

def criar_janela_entrada_nota_fiscal():

    janela_entrada_nota_fiscal = tk.Toplevel()
    janela_entrada_nota_fiscal.title("Entrada Nota Fiscal")
    janela_entrada_nota_fiscal.geometry("1100x600")

    label_data_entrada = tk.Label(janela_entrada_nota_fiscal, text="Data Entrada:", font=("Arial", 10, "bold"))
    label_data_entrada.place(x=26, y=10)

    entry_data_entrada = tk.Entry(janela_entrada_nota_fiscal, width=10, font=("Arial", 10, "bold"))
    entry_data_entrada.place(x=120, y=10)

    label_fornecedor = tk.Label(janela_entrada_nota_fiscal, text="Fornecedor:", font=("Arial", 10, "bold"))
    label_fornecedor.place(x=200, y=10)

    entry_codigo_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=6, font=("Arial", 10, "bold"))
    entry_codigo_fornecedor.place(x=285, y=10)

    entry_descricao_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=30, font=("Arial", 10, "bold"))
    entry_descricao_fornecedor.place(x=335, y=10)

    label_numero_nota_fiscal = tk.Label(janela_entrada_nota_fiscal, text="Número NF-e:", font=("Arial", 10, "bold"))
    label_numero_nota_fiscal.place(x=24, y=40)

    entry_numero_nota_fiscal = tk.Entry(janela_entrada_nota_fiscal, width=10, font=("Arial", 10, "bold"))
    entry_numero_nota_fiscal.place(x=120, y=40)
