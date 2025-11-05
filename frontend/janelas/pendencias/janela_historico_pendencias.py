import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

from backend.scripts.processar_pendencias_estoque import processar_pendencias

def criar_janela_historico_pendencias():

    def buscar_pendencias_gui():

        pendencias = processar_pendencias()

        for item in treeview_pendencias.get_children():
            treeview_pendencias.delete(item)

        for i, linha in pendencias.iterrows():
            treeview_pendencias.insert("", "end", values=list(linha))



    janela_historico_pendencias = tk.Toplevel()
    janela_historico_pendencias.title("Histórico Pendências")
    janela_historico_pendencias.geometry("1100x600")
    janela_historico_pendencias.resizable(False, False)


    label_cupom = tk.Label(janela_historico_pendencias, text="Cupom:", font=LABEL)
    label_cupom.place(x=75, y=20)

    entry_cupom = tk.Entry(janela_historico_pendencias, width=7, font=ENTRY)
    entry_cupom.place(x=130, y=20)

    label_cliente = tk.Label(janela_historico_pendencias, text="Cliente:", font=LABEL)
    label_cliente.place(x=195, y=20)

    entry_cliente = tk.Entry(janela_historico_pendencias, width=10, font=ENTRY)
    entry_cliente.place(x=250, y=20)

    label_data_ocorrencia = tk.Label(janela_historico_pendencias, text="Data Ocorrência:", font=LABEL)
    label_data_ocorrencia.place(x=335, y=20)

    entry_data_ocorrencia = tk.Entry(janela_historico_pendencias, width=10, font=ENTRY)
    entry_data_ocorrencia.place(x=450, y=20)

    label_razao_social = tk.Label(janela_historico_pendencias, text="Razão Social:", font=LABEL)
    label_razao_social.place(x=535, y=20)

    entry_razao_social = tk.Entry(janela_historico_pendencias, font=ENTRY)
    entry_razao_social.place(x=630, y=20)

    label_cidade = tk.Label(janela_historico_pendencias, text="Cidade:", font=LABEL)
    label_cidade.place(x=785, y=20)

    entry_cidade = tk.Entry(janela_historico_pendencias, width=8, font=ENTRY)
    entry_cidade.place(x=840, y=20)

    label_vendedor = tk.Label(janela_historico_pendencias, text="Vendedor:", font=LABEL)
    label_vendedor.place(x=910, y=20)

    entry_vendedor = tk.Entry(janela_historico_pendencias, width=3, font=ENTRY)
    entry_vendedor.place(x=985, y=20)

    label_codigo_produto = tk.Label(janela_historico_pendencias, text="Código Produto:", font=LABEL)
    label_codigo_produto.place(x=20, y=60)

    entry_codigo_produto = tk.Entry(janela_historico_pendencias, width=7, font=ENTRY)
    entry_codigo_produto.place(x=130, y=60)

    label_quantidade = tk.Label(janela_historico_pendencias, text="Quantidade:", font=LABEL)
    label_quantidade.place(x=195, y=60)

    entry_quantidade = tk.Entry(janela_historico_pendencias, width=5, font=ENTRY)
    entry_quantidade.place(x=285, y=60)


    botao_buscar_pendencias = tk.Button(janela_historico_pendencias, text="Buscar", font=BOTAO, command=buscar_pendencias_gui)
    botao_buscar_pendencias.place(x=360, y=55)


    linha_horizontal_superior = tk.Frame(janela_historico_pendencias, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=110)


    scrollbar_vertical = ttk.Scrollbar(janela_historico_pendencias, orient="vertical")
    scrollbar_vertical.place(x=1062, y=140, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("cupom", "data_ocorrencia", "cliente", "razao_social", "cidade", "vendedor", "codigo_produto", "quantidade")
    treeview_pendencias = ttk.Treeview(
        janela_historico_pendencias,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_pendencias.place(x=20, y=140, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_pendencias.yview)

    treeview_pendencias.heading("cupom", text="CUPOM", anchor="center")
    treeview_pendencias.heading("data_ocorrencia", text="DATA OCORRÊNCIA", anchor="center")
    treeview_pendencias.heading("cliente", text="CLIENTE", anchor="center")
    treeview_pendencias.heading("razao_social", text="RAZÃO SOCIAL", anchor="center")
    treeview_pendencias.heading("cidade", text="CIDADE", anchor="center")
    treeview_pendencias.heading("vendedor", text="VENDEDOR", anchor="center")
    treeview_pendencias.heading("codigo_produto", text="CÓDIGO PRODUTO", anchor="center")
    treeview_pendencias.heading("quantidade", text="QUANTIDADE", anchor="center")

    treeview_pendencias.column("cupom", width=60, anchor="center")
    treeview_pendencias.column("data_ocorrencia", width=128, anchor="center")
    treeview_pendencias.column("cliente", width=88, anchor="center")
    treeview_pendencias.column("razao_social", width=198, anchor="center")
    treeview_pendencias.column("cidade", width=128, anchor="center")
    treeview_pendencias.column("vendedor", width=90, anchor="center")
    treeview_pendencias.column("codigo_produto", width=128, anchor="center")
    treeview_pendencias.column("quantidade", width=128, anchor="center")
    # endregion


    linha_horizontal_inferior = tk.Frame(janela_historico_pendencias, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)


    lista_entrys = [
        entry_cupom,
        entry_cliente,
        entry_data_ocorrencia,
        entry_razao_social,
        entry_cidade,
        entry_vendedor,
        entry_codigo_produto,
        entry_quantidade,
        botao_buscar_pendencias
    ]

    configurar_binds(lista_entrys, acoes_intermediarias=None, ultima_acao=buscar_pendencias_gui)
