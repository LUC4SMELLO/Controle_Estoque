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

    entry_descricao_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=53, font=("Arial", 10, "bold"))
    entry_descricao_fornecedor.place(x=335, y=10)

    label_uf = tk.Label(janela_entrada_nota_fiscal, text="UF:", font=("Arial", 10, "bold"))
    label_uf.place(x=256, y=40)

    entry_uf = tk.Entry(janela_entrada_nota_fiscal, width=6, font=("Arial", 10, "bold"))
    entry_uf.place(x=285, y=40)

    label_municipio = tk.Label(janela_entrada_nota_fiscal, text="Município:", font=("Arial", 10, "bold"))
    label_municipio.place(x=332, y=40)

    entry_municipio = tk.Entry(janela_entrada_nota_fiscal, font=("Arial", 10, "bold"))
    entry_municipio.place(x=405, y=40)

    label_bairro = tk.Label(janela_entrada_nota_fiscal, text="Bairro:", font=("Arial", 10, "bold"))
    label_bairro.place(x=515, y=40)

    entry_bairro = tk.Entry(janela_entrada_nota_fiscal, font=("Arial", 10, "bold"))
    entry_bairro.place(x=565, y=40)

    label_numero_nota_fiscal = tk.Label(janela_entrada_nota_fiscal, text="Número NF-e:", font=("Arial", 10, "bold"))
    label_numero_nota_fiscal.place(x=24, y=40)

    entry_numero_nota_fiscal = tk.Entry(janela_entrada_nota_fiscal, width=10, font=("Arial", 10, "bold"))
    entry_numero_nota_fiscal.place(x=120, y=40)

    botao_buscar_nota_fiscal = tk.Button(janela_entrada_nota_fiscal, text="Buscar\nNota Fiscal", font=("Arial", 10, "bold"))
    botao_buscar_nota_fiscal.place(x=1000, y=10)

    linha_horizontal_superior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)

    # TREEVIEW

    treeview = ttk.Treeview()
    treeview.column("numero_item", "codigo_item", "descricao", "quantidade")
    treeview.heading("numero_item", text="Nº ITEM")
    treeview.heading("codigo_item", text="CÓDIGO ITEM")
    treeview.heading("descricao", text="DESCRIÇÃO")
    treeview.heading("quantidade", text="QUANTIDADE")   
    treeview.place(x=10, y=110)




    linha_horizontal_inferior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_entrada = tk.Button(janela_entrada_nota_fiscal, text="Confirmar", font=("Arial", 10, "bold"))
    botao_confirmar_entrada.place(x=900, y=565)

    botao_cancelar_saida = tk.Button(janela_entrada_nota_fiscal, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_saida.place(x=1000, y=565)

