import tkinter as tk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

from backend.controladores.fornecedor.consultar_fornecedor_controlador import buscar_fornecedor_back

from backend.controladores.fornecedor.excluir_fornecedor_controlador import excluir_fornecedor_back

from backend.validadores.fornecedor.formulario_fornecedor import validar_formulario_fornecedor

fornecedor_buscado = False

def criar_janela_excluir_fornecedor():

    def buscar_fornecedor_excluir_gui():

        global fornecedor_buscado
        
        entry_razao_social_excluir.delete(0, tk.END)
        entry_nome_fantasia_excluir.delete(0, tk.END)
        fornecedor_ativo.set(False)
        entry_cnpj_excluir.delete(0, tk.END)
        entry_inscricao_estadual_excluir.delete(0, tk.END)
        entry_logradouro_excluir.delete(0, tk.END)
        entry_bairro_excluir.delete(0, tk.END)
        entry_cidade_excluir.delete(0, tk.END)
        entry_cep_excluir.delete(0, tk.END)
        entry_estado_excluir.delete(0, tk.END)

        valido, resposta = buscar_fornecedor_back(entry_codigo_excluir.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            entry_codigo_excluir.focus_set()
            return None

        entry_razao_social_excluir.insert(0, resposta.razao_social)
        entry_nome_fantasia_excluir.insert(0, resposta.nome_fantasia)
        fornecedor_ativo.set(resposta.fornecedor_ativo)
        entry_cnpj_excluir.insert(0, resposta.cnpj)
        entry_inscricao_estadual_excluir.insert(0, resposta.inscricao_estadual)
        entry_logradouro_excluir.insert(0, resposta.logradouro)
        entry_bairro_excluir.insert(0, resposta.bairro)
        entry_cidade_excluir.insert(0, resposta.cidade)
        entry_cep_excluir.insert(0, resposta.cep)
        entry_estado_excluir.insert(0, resposta.estado)

        fornecedor_buscado = True

    def excluir_fornecedor_gui():

        global fornecedor_buscado

        if not fornecedor_buscado:
            messagebox.showerror("Erro.", "Busque o Fornecedor Primeiro.")
            entry_codigo_excluir.focus_set()
            return None
        
        valido, mensagem = validar_formulario_fornecedor(
        entry_codigo_excluir.get().strip(),
        entry_razao_social_excluir.get().strip(),
        entry_nome_fantasia_excluir.get().strip(),
        entry_cnpj_excluir.get().strip(),
        entry_inscricao_estadual_excluir.get().strip(),
        entry_logradouro_excluir.get().strip(),
        entry_bairro_excluir.get().strip(),
        entry_cidade_excluir.get().strip(),
        entry_cep_excluir.get().strip(),
        entry_estado_excluir.get().strip()
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_excluir.focus_set()
            return None

        excluir_fornecedor_back(
            entry_codigo_excluir.get()
        )
        messagebox.showinfo("Sucesso!", "Fornecedor Excluído!")
        entry_codigo_excluir.focus_set()

        entry_codigo_excluir.delete(0, tk.END)
        entry_razao_social_excluir.delete(0, tk.END)
        entry_nome_fantasia_excluir.delete(0, tk.END)
        fornecedor_ativo.set(False)
        entry_cnpj_excluir.delete(0, tk.END)
        entry_inscricao_estadual_excluir.delete(0, tk.END)
        entry_logradouro_excluir.delete(0, tk.END)
        entry_bairro_excluir.delete(0, tk.END)
        entry_cidade_excluir.delete(0, tk.END)
        entry_cep_excluir.delete(0, tk.END)
        entry_estado_excluir.delete(0, tk.END)

    def fechar_janela_excluir_fornecedor():

        global fornecedor_buscado 

        janela_excluir_fornecedor.destroy()

        fornecedor_buscado = False

    janela_excluir_fornecedor = tk.Toplevel()
    janela_excluir_fornecedor.title("Excluir Fornecedor")
    janela_excluir_fornecedor.geometry("800x600")

    linha_horizontal_superior = tk.Frame(janela_excluir_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_excluir = tk.Label(janela_excluir_fornecedor, text="Código:", font=LABEL)
    label_codigo_excluir.place(x=58, y=10)

    botao_buscar_excluir = tk.Button(janela_excluir_fornecedor, text="Buscar", font=BOTAO, command=buscar_fornecedor_excluir_gui)
    botao_buscar_excluir.place(x=175, y=5)

    entry_codigo_excluir = tk.Entry(janela_excluir_fornecedor, width=7 ,font=ENTRY)
    entry_codigo_excluir.place(x=115, y=10)

    label_razao_social_excluir = tk.Label(janela_excluir_fornecedor, text="Razão Social:", font=LABEL)
    label_razao_social_excluir.place(x=20, y=40)

    entry_razao_social_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY, width=60)
    entry_razao_social_excluir.place(x=115, y=40)

    label_excluir_ativo = tk.Label(janela_excluir_fornecedor, text="Ativo:", font=LABEL)
    label_excluir_ativo.place(x=710, y=40)

    fornecedor_ativo = tk.BooleanVar()
    entry_excluir_ativo_excluir = tk.Checkbutton(janela_excluir_fornecedor, variable=fornecedor_ativo)
    entry_excluir_ativo_excluir.place(x=750, y=40)

    label_nome_fantasia_excluir = tk.Label(janela_excluir_fornecedor, text="Nome Fantasia:", font=LABEL)
    label_nome_fantasia_excluir.place(x=10, y=100)

    entry_nome_fantasia_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY, width=60)
    entry_nome_fantasia_excluir.place(x=115, y=100)

    label_endereco_excluir = tk.Label(janela_excluir_fornecedor, text="Endereço:", font=("Arial", 12, "bold"))
    label_endereco_excluir.place(x=30, y=140)

    label_logradouro_excluir = tk.Label(janela_excluir_fornecedor, text="Logradouro:", font=LABEL)
    label_logradouro_excluir.place(x=30, y=170)

    entry_logradouro_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_logradouro_excluir.place(x=115, y=170)

    label_bairro_excluir = tk.Label(janela_excluir_fornecedor, text="Bairro:", font=LABEL)
    label_bairro_excluir.place(x=60, y=200)

    entry_bairro_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_bairro_excluir.place(x=115, y=200)

    label_cidade_excluir = tk.Label(janela_excluir_fornecedor, text="Cidade:", font=LABEL)
    label_cidade_excluir.place(x=55, y=230)

    entry_cidade_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_cidade_excluir.place(x=115, y=230)

    label_cep_excluir = tk.Label(janela_excluir_fornecedor, text="CEP:", font=LABEL)
    label_cep_excluir.place(x=75, y=260)

    entry_cep_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_cep_excluir.place(x=115, y=260)

    label_estado_excluir = tk.Label(janela_excluir_fornecedor, text="Estado:", font=LABEL)
    label_estado_excluir.place(x=60, y=290)

    entry_estado_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_estado_excluir.place(x=115, y=290)

    label_cnpj_excluir = tk.Label(janela_excluir_fornecedor, text="CNPJ:", font=LABEL)
    label_cnpj_excluir.place(x=585, y=170)

    entry_cnpj_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_cnpj_excluir.place(x=630, y=170)

    label_inscricao_estadual_excluir = tk.Label(janela_excluir_fornecedor, text="Inscrição Estadual:", font=LABEL)
    label_inscricao_estadual_excluir.place(x=505, y=200)

    entry_inscricao_estadual_excluir = tk.Entry(janela_excluir_fornecedor, font=ENTRY)
    entry_inscricao_estadual_excluir.place(x=630, y=200)



    linha_horizontal_inferior = tk.Frame(janela_excluir_fornecedor, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_excluir = tk.Button(janela_excluir_fornecedor, text="Confirmar", font=BOTAO, command=excluir_fornecedor_gui)
    botao_confirmar_excluir.place(x=600, y=565)

    botao_cancelar_excluir =  tk.Button(janela_excluir_fornecedor, text="Cancelar", font=BOTAO, command=fechar_janela_excluir_fornecedor)
    botao_cancelar_excluir.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_excluir,
        botao_buscar_excluir,
        entry_razao_social_excluir,
        entry_nome_fantasia_excluir,
        entry_logradouro_excluir,
        entry_bairro_excluir,
        entry_cidade_excluir,
        entry_cep_excluir,
        entry_estado_excluir,
        entry_cnpj_excluir,
        entry_inscricao_estadual_excluir,
    ]

    acoes_intermediarias = [None, buscar_fornecedor_excluir_gui, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias=acoes_intermediarias, ultima_acao=None)