import tkinter as tk
from tkinter import messagebox, ttk

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

def criar_janela_cadastrar_fornecedor():

    janela_cadastrar_fornecedor = tk.Toplevel()
    janela_cadastrar_fornecedor.title("Cadastrar Fornecedor")
    janela_cadastrar_fornecedor.geometry("800x600")

    linha_horizontal_superior = tk.Frame(janela_cadastrar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Código:", font=LABEL)
    label_codigo_fornecedor.place(x=58, y=10)

    entry_codigo_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_codigo_fornecedor.place(x=115, y=10)

    label_razao_social_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Razão Social:", font=LABEL)
    label_razao_social_fornecedor.place(x=20, y=40)

    entry_razao_social_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY, width=60)
    entry_razao_social_fornecedor.place(x=115, y=40)

    label_fornecedor_ativo = tk.Label(janela_cadastrar_fornecedor, text="Ativo:", font=LABEL)
    label_fornecedor_ativo.place(x=710, y=40)

    fornecedor_ativo = tk.BooleanVar()
    entry_fornecedor_ativo = tk.Checkbutton(janela_cadastrar_fornecedor, variable=fornecedor_ativo)
    entry_fornecedor_ativo.place(x=750, y=40)

    label_nome_fantasia = tk.Label(janela_cadastrar_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia.place(x=10, y=100)

    entry_nome_fantasia = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia.place(x=115, y=100)


    label_endereco_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_fornecedor.place(x=10, y=140)

    label_logradouro_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_fornecedor.place(x=10, y=170)

    entry_logradouro_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_logradouro_fornecedor.place(x=115, y=170)

    label_bairro_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_fornecedor.place(x=10, y=200)

    entry_bairro_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_bairro_fornecedor.place(x=115, y=200)

    label_cidade = tk.Label(janela_cadastrar_fornecedor, text="Cidade:", font=LABEL)
    label_cidade.place(x=10, y=200)

    entry_cidade = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_cidade.place(x=115, y=200)

    label_cep = tk.Label(janela_cadastrar_fornecedor, text="CEP:", font=LABEL)
    


    label_cnpj_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="CNPJ:", font=LABEL)
    label_cnpj_fornecedor.place(x=585, y=170)

    entry_cnpj_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_cnpj_fornecedor.place(x=630, y=170)

    label_inscricao_estadual = tk.Label(janela_cadastrar_fornecedor, text="Inscrição Estadual:", font=LABEL)
    label_inscricao_estadual.place(x=505, y=200)

    entry_inscricao_estadual = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_inscricao_estadual.place(x=630, y=200)



    linha_horizontal_inferior = tk.Frame(janela_cadastrar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_cadastro = tk.Button(janela_cadastrar_fornecedor, text="Confirmar", font=BOTAO)
    botao_confirmar_cadastro.place(x=600, y=565)

    botao_cancelar_cadastro =  tk.Button(janela_cadastrar_fornecedor, text="Cancelar", font=BOTAO)
    botao_cancelar_cadastro.place(x=700, y=565)