import tkinter as tk

from backend.constantes.fontes import LABEL, ENTRY, BOTAO


def criar_janela_alterar_fornecedor():

    janela_alterar_fornecedor = tk.Toplevel()
    janela_alterar_fornecedor.title("Alterar Fornecedor")
    janela_alterar_fornecedor.geometry("800x600")

    linha_horizontal_superior = tk.Frame(janela_alterar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_alterar = tk.Label(janela_alterar_fornecedor, text="Código:", font=LABEL)
    label_codigo_alterar.place(x=58, y=10)

    botao_buscar_fornecedor = tk.Button(janela_alterar_fornecedor, text="Buscar", font=BOTAO)
    botao_buscar_fornecedor.place(x=175, y=5)

    entry_codigo_alterar = tk.Entry(janela_alterar_fornecedor, width=7 ,font=ENTRY)
    entry_codigo_alterar.place(x=115, y=10)

    label_razao_social_alterar = tk.Label(janela_alterar_fornecedor, text="Razão Social:", font=LABEL)
    label_razao_social_alterar.place(x=20, y=40)

    entry_razao_social_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=60)
    entry_razao_social_alterar.place(x=115, y=40)

    label_fornecedor_ativo = tk.Label(janela_alterar_fornecedor, text="Ativo:", font=LABEL)
    label_fornecedor_ativo.place(x=710, y=40)

    fornecedor_ativo = tk.BooleanVar()
    entry_fornecedor_ativo_fornecedor = tk.Checkbutton(janela_alterar_fornecedor, variable=fornecedor_ativo)
    entry_fornecedor_ativo_fornecedor.place(x=750, y=40)

    label_nome_fantasia_alterar = tk.Label(janela_alterar_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia_alterar.place(x=10, y=100)

    entry_nome_fantasia_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia_alterar.place(x=115, y=100)

    label_endereco_alterar = tk.Label(janela_alterar_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_alterar.place(x=30, y=140)

    label_logradouro_alterar = tk.Label(janela_alterar_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_alterar.place(x=30, y=170)

    entry_logradouro_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_logradouro_alterar.place(x=115, y=170)

    label_bairro_alterar = tk.Label(janela_alterar_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_alterar.place(x=60, y=200)

    entry_bairro_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_bairro_alterar.place(x=115, y=200)

    label_cidade_alterar = tk.Label(janela_alterar_fornecedor, text="Cidade:", font=LABEL)
    label_cidade_alterar.place(x=55, y=230)

    entry_cidade_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_cidade_alterar.place(x=115, y=230)

    label_cep_alterar = tk.Label(janela_alterar_fornecedor, text="CEP:", font=LABEL)
    label_cep_alterar.place(x=75, y=260)

    entry_cep_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_cep_alterar.place(x=115, y=260)

    label_estado_alterar = tk.Label(janela_alterar_fornecedor, text="Estado:", font=LABEL)
    label_estado_alterar.place(x=60, y=290)

    entry_estado_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_estado_alterar.place(x=115, y=290)

    label_cnpj_alterar = tk.Label(janela_alterar_fornecedor, text="CNPJ:", font=LABEL)
    label_cnpj_alterar.place(x=585, y=170)

    entry_cnpj_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_cnpj_alterar.place(x=630, y=170)

    label_inscricao_estadual_alterar = tk.Label(janela_alterar_fornecedor, text="Inscrição Estadual:", font=LABEL)
    label_inscricao_estadual_alterar.place(x=505, y=200)

    entry_inscricao_estadual_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY)
    entry_inscricao_estadual_alterar.place(x=630, y=200)



    linha_horizontal_inferior = tk.Frame(janela_alterar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_alterar = tk.Button(janela_alterar_fornecedor, text="Confirmar", font=BOTAO)
    botao_confirmar_alterar.place(x=600, y=565)

    botao_cancelar_alterar =  tk.Button(janela_alterar_fornecedor, text="Cancelar", font=BOTAO)
    botao_cancelar_alterar.place(x=700, y=565)