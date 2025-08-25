import tkinter as tk
from tkinter import  messagebox

from backend.binds.configuracao_binds import configurar_binds

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.controladores.fornecedor.consultar_fornecedor_controlador import buscar_fornecedor_back

def criar_janela_consultar_fornecedor():

    def buscar_fornecedor_gui():

        
        entry_razao_social_consultar.delete(0, tk.END)
        entry_nome_fantasia_consultar.delete(0, tk.END)
        fornecedor_ativo.set(False)
        entry_cnpj_consultar.delete(0, tk.END)
        entry_inscricao_estadual_consultar.delete(0, tk.END)
        entry_logradouro_consultar.delete(0, tk.END)
        entry_bairro_consultar.delete(0, tk.END)
        entry_cidade_consultar.delete(0, tk.END)
        entry_cep_consultar.delete(0, tk.END)
        entry_estado_consultar.delete(0, tk.END)

        valido, resposta = buscar_fornecedor_back(entry_codigo_consultar.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            entry_codigo_consultar.focus_set()
            return None

        entry_razao_social_consultar.insert(0, resposta.razao_social)
        entry_nome_fantasia_consultar.insert(0, resposta.nome_fantasia)
        fornecedor_ativo.set(resposta.fornecedor_ativo)
        entry_cnpj_consultar.insert(0, resposta.cnpj)
        entry_inscricao_estadual_consultar.insert(0, resposta.inscricao_estadual)
        entry_logradouro_consultar.insert(0, resposta.logradouro)
        entry_bairro_consultar.insert(0, resposta.bairro)
        entry_cidade_consultar.insert(0, resposta.cidade)
        entry_cep_consultar.insert(0, resposta.cep)
        entry_estado_consultar.insert(0, resposta.estado)




    janela_consultar_fornecedor = tk.Toplevel()
    janela_consultar_fornecedor.title("Consultar Fornecedor")
    janela_consultar_fornecedor.geometry("800x600")

    linha_horizontal_superior = tk.Frame(janela_consultar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_consultar = tk.Label(janela_consultar_fornecedor, text="Código:", font=LABEL)
    label_codigo_consultar.place(x=58, y=10)

    botao_buscar_fornecedor = tk.Button(janela_consultar_fornecedor, text="Buscar", font=BOTAO, command=buscar_fornecedor_gui)
    botao_buscar_fornecedor.place(x=175, y=5)

    entry_codigo_consultar = tk.Entry(janela_consultar_fornecedor, width=7 ,font=ENTRY)
    entry_codigo_consultar.place(x=115, y=10)

    label_razao_social_consultar = tk.Label(janela_consultar_fornecedor, text="Razão Social:", font=LABEL)
    label_razao_social_consultar.place(x=20, y=40)

    entry_razao_social_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY, width=60)
    entry_razao_social_consultar.place(x=115, y=40)

    label_fornecedor_ativo = tk.Label(janela_consultar_fornecedor, text="Ativo:", font=LABEL)
    label_fornecedor_ativo.place(x=710, y=40)

    fornecedor_ativo = tk.BooleanVar()
    entry_fornecedor_ativo_fornecedor = tk.Checkbutton(janela_consultar_fornecedor, variable=fornecedor_ativo)
    entry_fornecedor_ativo_fornecedor.place(x=750, y=40)

    label_nome_fantasia_consultar = tk.Label(janela_consultar_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia_consultar.place(x=10, y=100)

    entry_nome_fantasia_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia_consultar.place(x=115, y=100)

    label_endereco_consultar = tk.Label(janela_consultar_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_consultar.place(x=30, y=140)

    label_logradouro_consultar = tk.Label(janela_consultar_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_consultar.place(x=30, y=170)

    entry_logradouro_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY, width=45)
    entry_logradouro_consultar.place(x=115, y=170)

    label_bairro_consultar = tk.Label(janela_consultar_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_consultar.place(x=60, y=200)

    entry_bairro_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY, width=45)
    entry_bairro_consultar.place(x=115, y=200)

    label_cidade_consultar = tk.Label(janela_consultar_fornecedor, text="Cidade:", font=LABEL)
    label_cidade_consultar.place(x=55, y=230)

    entry_cidade_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY)
    entry_cidade_consultar.place(x=115, y=230)

    label_cep_consultar = tk.Label(janela_consultar_fornecedor, text="CEP:", font=LABEL)
    label_cep_consultar.place(x=75, y=260)

    entry_cep_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY)
    entry_cep_consultar.place(x=115, y=260)

    label_estado_consultar = tk.Label(janela_consultar_fornecedor, text="Estado:", font=LABEL)
    label_estado_consultar.place(x=60, y=290)

    entry_estado_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY)
    entry_estado_consultar.place(x=115, y=290)

    label_cnpj_consultar = tk.Label(janela_consultar_fornecedor, text="CNPJ:", font=LABEL)
    label_cnpj_consultar.place(x=585, y=170)

    entry_cnpj_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY)
    entry_cnpj_consultar.place(x=630, y=170)

    label_inscricao_estadual_consultar = tk.Label(janela_consultar_fornecedor, text="Inscrição Estadual:", font=LABEL)
    label_inscricao_estadual_consultar.place(x=505, y=200)

    entry_inscricao_estadual_consultar = tk.Entry(janela_consultar_fornecedor, font=ENTRY)
    entry_inscricao_estadual_consultar.place(x=630, y=200)



    linha_horizontal_inferior = tk.Frame(janela_consultar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_consulta = tk.Button(janela_consultar_fornecedor, text="Confirmar", font=BOTAO)
    botao_confirmar_consulta.place(x=600, y=565)

    botao_cancelar_cadastro =  tk.Button(janela_consultar_fornecedor, text="Cancelar", font=BOTAO)
    botao_cancelar_cadastro.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_consultar,
        botao_buscar_fornecedor,
        entry_razao_social_consultar,
        entry_nome_fantasia_consultar,
        entry_logradouro_consultar,
        entry_bairro_consultar,
        entry_cidade_consultar,
        entry_cep_consultar,
        entry_estado_consultar,
        entry_cnpj_consultar,
        entry_inscricao_estadual_consultar,
        botao_confirmar_consulta
    ]

    acoes_intermediarias = [None, buscar_fornecedor_gui, None, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias=acoes_intermediarias, ultima_acao=None)