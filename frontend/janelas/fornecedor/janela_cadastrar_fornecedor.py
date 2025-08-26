import tkinter as tk
from tkinter import messagebox, ttk

from backend.binds.configuracao_binds import configurar_binds

from backend.validadores.fornecedor.formulario_fornecedor import validar_formulario_fornecedor

from backend.controladores.fornecedor.cadastrar_fornecedor_controlador import cadastrar_fornecedor_back

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

def criar_janela_cadastrar_fornecedor():

    def cadastrar_fornecedor_gui():

        valido, mensagem = validar_formulario_fornecedor(
            entry_codigo_fornecedor.get().strip(),
            entry_razao_social_fornecedor.get().strip(),
            entry_nome_fantasia_fornecedor.get().strip(),
            entry_cnpj_fornecedor.get().strip(),
            entry_inscricao_estadual_fornecedor.get().strip(),
            entry_logradouro_fornecedor.get().strip(),
            entry_bairro_fornecedor.get().strip(),
            entry_cidade_fornecedor.get().strip(),
            entry_cep_fornecedor.get().strip(),
            entry_estado.get().strip()
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_fornecedor.focus_set()
            return None
        
        cnpj_limpo = entry_cnpj_fornecedor.get().strip().replace(".", "").replace("/", "").replace("-", "")

        cadastrar_fornecedor_back(
            entry_codigo_fornecedor.get().strip(),
            entry_razao_social_fornecedor.get().strip(),
            entry_nome_fantasia_fornecedor.get().strip(),
            fornecedor_ativo.get(),
            cnpj_limpo,
            entry_inscricao_estadual_fornecedor.get().strip(),
            entry_logradouro_fornecedor.get().strip(),
            entry_bairro_fornecedor.get().strip(),
            entry_cidade_fornecedor.get().strip(),
            entry_cep_fornecedor.get().strip(),
            entry_estado.get().strip()
        )

        messagebox.showinfo("Sucesso!", "Fornecedor Cadastrado!")
        entry_codigo_fornecedor.focus_set()

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

    label_nome_fantasia_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia_fornecedor.place(x=10, y=100)

    entry_nome_fantasia_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia_fornecedor.place(x=115, y=100)

    label_endereco_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_fornecedor.place(x=30, y=140)

    label_logradouro_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_fornecedor.place(x=30, y=170)

    entry_logradouro_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY, width=45)
    entry_logradouro_fornecedor.place(x=115, y=170)

    label_bairro_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_fornecedor.place(x=60, y=200)

    entry_bairro_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY, width=45)
    entry_bairro_fornecedor.place(x=115, y=200)

    label_cidade_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Cidade:", font=LABEL)
    label_cidade_fornecedor.place(x=55, y=230)

    entry_cidade_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_cidade_fornecedor.place(x=115, y=230)

    label_cep_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="CEP:", font=LABEL)
    label_cep_fornecedor.place(x=75, y=260)

    entry_cep_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_cep_fornecedor.place(x=115, y=260)

    label_estado_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Estado:", font=LABEL)
    label_estado_fornecedor.place(x=60, y=290)

    entry_estado = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_estado.place(x=115, y=290)

    label_cnpj_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="CNPJ:", font=LABEL)
    label_cnpj_fornecedor.place(x=585, y=170)

    entry_cnpj_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_cnpj_fornecedor.place(x=630, y=170)

    label_inscricao_estadual_fornecedor = tk.Label(janela_cadastrar_fornecedor, text="Inscrição Estadual:", font=LABEL)
    label_inscricao_estadual_fornecedor.place(x=505, y=200)

    entry_inscricao_estadual_fornecedor = tk.Entry(janela_cadastrar_fornecedor, font=ENTRY)
    entry_inscricao_estadual_fornecedor.place(x=630, y=200)



    linha_horizontal_inferior = tk.Frame(janela_cadastrar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_cadastro = tk.Button(janela_cadastrar_fornecedor, text="Confirmar", font=BOTAO, command=cadastrar_fornecedor_gui)
    botao_confirmar_cadastro.place(x=600, y=565)

    botao_cancelar_cadastro =  tk.Button(janela_cadastrar_fornecedor, text="Cancelar", font=BOTAO)
    botao_cancelar_cadastro.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_fornecedor,
        entry_razao_social_fornecedor,
        entry_nome_fantasia_fornecedor,
        entry_logradouro_fornecedor,
        entry_bairro_fornecedor,
        entry_cidade_fornecedor,
        entry_cep_fornecedor,
        entry_estado,
        entry_cnpj_fornecedor,
        entry_inscricao_estadual_fornecedor,
        botao_confirmar_cadastro
    ]

    configurar_binds(lista_entrys, acoes_intermediarias=None, ultima_acao=cadastrar_fornecedor_gui)