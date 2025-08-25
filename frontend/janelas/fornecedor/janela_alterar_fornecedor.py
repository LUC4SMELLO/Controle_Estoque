import tkinter as tk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

from backend.controladores.fornecedor.consultar_fornecedor_controlador import buscar_fornecedor_back

from backend.validadores.fornecedor.formulario_fornecedor import validar_formulario_fornecedor

from backend.controladores.fornecedor.alterar_fornecedor_controlador import alterar_fornecedor_back


fornecedor_buscado = False

def criar_janela_alterar_fornecedor():

    def buscar_fornecedor_alterar_gui():

        global fornecedor_buscado
        
        entry_razao_social_alterar.delete(0, tk.END)
        entry_nome_fantasia_alterar.delete(0, tk.END)
        fornecedor_ativo.set(False)
        entry_cnpj_alterar.delete(0, tk.END)
        entry_inscricao_estadual_alterar.delete(0, tk.END)
        entry_logradouro_alterar.delete(0, tk.END)
        entry_bairro_alterar.delete(0, tk.END)
        entry_cidade_alterar.delete(0, tk.END)
        entry_cep_alterar.delete(0, tk.END)
        entry_estado_alterar.delete(0, tk.END)

        valido, resposta = buscar_fornecedor_back(entry_codigo_alterar.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            entry_codigo_alterar.focus_set()
            return None

        entry_razao_social_alterar.insert(0, resposta.razao_social)
        entry_nome_fantasia_alterar.insert(0, resposta.nome_fantasia)
        fornecedor_ativo.set(resposta.fornecedor_ativo)
        entry_cnpj_alterar.insert(0, resposta.cnpj)
        entry_inscricao_estadual_alterar.insert(0, resposta.inscricao_estadual)
        entry_logradouro_alterar.insert(0, resposta.logradouro)
        entry_bairro_alterar.insert(0, resposta.bairro)
        entry_cidade_alterar.insert(0, resposta.cidade)
        entry_cep_alterar.insert(0, resposta.cep)
        entry_estado_alterar.insert(0, resposta.estado)

        fornecedor_buscado = True

    def alterar_fornecedor_gui():

        global fornecedor_buscado

        if not fornecedor_buscado:
            messagebox.showerror("Erro.", "Busque o Fornecedor Primeiro.")
            entry_codigo_alterar.focus_set()
            return None
        
        valido, mensagem = validar_formulario_fornecedor(
        entry_codigo_alterar.get().strip(),
        entry_razao_social_alterar.get().strip(),
        entry_nome_fantasia_alterar.get().strip(),
        entry_cnpj_alterar.get().strip(),
        entry_inscricao_estadual_alterar.get().strip(),
        entry_logradouro_alterar.get().strip(),
        entry_bairro_alterar.get().strip(),
        entry_cidade_alterar.get().strip(),
        entry_cep_alterar.get().strip(),
        entry_estado_alterar.get().strip()
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_alterar.focus_set()
            return None

        alterar_fornecedor_back(
            entry_codigo_alterar.get(),
            entry_razao_social_alterar.get(),
            entry_nome_fantasia_alterar.get(),
            fornecedor_ativo.get(),
            entry_cnpj_alterar.get(),
            entry_inscricao_estadual_alterar.get(),
            entry_logradouro_alterar.get(),
            entry_bairro_alterar.get(),
            entry_cidade_alterar.get(),
            entry_cep_alterar.get(),
            entry_estado_alterar.get()
        )
        messagebox.showinfo("Sucesso!", "Fornecedor Atualizado!")
        entry_codigo_alterar.focus_set()

        entry_codigo_alterar.delete(0, tk.END)
        entry_razao_social_alterar.delete(0, tk.END)
        entry_nome_fantasia_alterar.delete(0, tk.END)
        fornecedor_ativo.set(False)
        entry_cnpj_alterar.delete(0, tk.END)
        entry_inscricao_estadual_alterar.delete(0, tk.END)
        entry_logradouro_alterar.delete(0, tk.END)
        entry_bairro_alterar.delete(0, tk.END)
        entry_cidade_alterar.delete(0, tk.END)
        entry_cep_alterar.delete(0, tk.END)
        entry_estado_alterar.delete(0, tk.END)


        fornecedor_buscado = False

    def fechar_janela_alterar_fornecedor():

        global fornecedor_buscado

        janela_alterar_fornecedor.destroy()

        fornecedor_buscado = False



    janela_alterar_fornecedor = tk.Toplevel()
    janela_alterar_fornecedor.title("Alterar Fornecedor")
    janela_alterar_fornecedor.geometry("800x600")

    linha_horizontal_superior = tk.Frame(janela_alterar_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_alterar = tk.Label(janela_alterar_fornecedor, text="Código:", font=LABEL)
    label_codigo_alterar.place(x=58, y=10)

    botao_buscar_alterar = tk.Button(janela_alterar_fornecedor, text="Buscar", font=BOTAO, command=buscar_fornecedor_alterar_gui)
    botao_buscar_alterar.place(x=175, y=5)

    entry_codigo_alterar = tk.Entry(janela_alterar_fornecedor, width=7 ,font=ENTRY)
    entry_codigo_alterar.place(x=115, y=10)

    label_razao_social_alterar = tk.Label(janela_alterar_fornecedor, text="Razão Social:", font=LABEL)
    label_razao_social_alterar.place(x=20, y=40)

    entry_razao_social_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=60)
    entry_razao_social_alterar.place(x=115, y=40)

    label_alterar_ativo = tk.Label(janela_alterar_fornecedor, text="Ativo:", font=LABEL)
    label_alterar_ativo.place(x=710, y=40)

    fornecedor_ativo = tk.BooleanVar()
    entry_alterar_ativo_alterar = tk.Checkbutton(janela_alterar_fornecedor, variable=fornecedor_ativo)
    entry_alterar_ativo_alterar.place(x=750, y=40)

    label_nome_fantasia_alterar = tk.Label(janela_alterar_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia_alterar.place(x=10, y=100)

    entry_nome_fantasia_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia_alterar.place(x=115, y=100)

    label_endereco_alterar = tk.Label(janela_alterar_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_alterar.place(x=30, y=140)

    label_logradouro_alterar = tk.Label(janela_alterar_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_alterar.place(x=30, y=170)

    entry_logradouro_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=45)
    entry_logradouro_alterar.place(x=115, y=170)

    label_bairro_alterar = tk.Label(janela_alterar_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_alterar.place(x=60, y=200)

    entry_bairro_alterar = tk.Entry(janela_alterar_fornecedor, font=ENTRY, width=45)
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

    botao_confirmar_alterar = tk.Button(janela_alterar_fornecedor, text="Confirmar", font=BOTAO, command=alterar_fornecedor_gui)
    botao_confirmar_alterar.place(x=600, y=565)

    botao_cancelar_alterar =  tk.Button(janela_alterar_fornecedor, text="Cancelar", font=BOTAO, command=fechar_janela_alterar_fornecedor)
    botao_cancelar_alterar.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_alterar,
        botao_buscar_alterar,
        entry_razao_social_alterar,
        entry_nome_fantasia_alterar,
        entry_logradouro_alterar,
        entry_bairro_alterar,
        entry_cidade_alterar,
        entry_cep_alterar,
        entry_estado_alterar,
        entry_cnpj_alterar,
        entry_inscricao_estadual_alterar,
        botao_confirmar_alterar
    ]

    acoes_intermediarias = [None, buscar_fornecedor_alterar_gui, None, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias=acoes_intermediarias, ultima_acao=alterar_fornecedor_gui)