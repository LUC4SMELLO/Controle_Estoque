import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

def criar_janela_historico_pendencias():

    janela_historico_pendencias = tk.Toplevel()
    janela_historico_pendencias.title("Histórico Pendências")
    janela_historico_pendencias.geometry("1100x600")
    janela_historico_pendencias.resizable(False, False)

    label_cupom = tk.Label(janela_historico_pendencias, text="Cupom:", font=LABEL)
    label_cupom.place(x=20, y=20)

    entry_cupom = tk.Entry(janela_historico_pendencias, width=10, font=ENTRY)
    entry_cupom.place(x=75, y=20)



    


    linha_horizontal_superior = tk.Frame(janela_historico_pendencias, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)




    scrollbar_vertical = ttk.Scrollbar(janela_historico_pendencias, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("cupom", "cliente", "data_ocorrencia", "razao_social", "cidade", "vendedor", "codigo_produto", "quantidade")
    treeview_pendencias = ttk.Treeview(
        janela_historico_pendencias,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_pendencias.place(x=20, y=110, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_pendencias.yview)

    treeview_pendencias.heading("cupom", text="CUPOM", anchor="center")
    treeview_pendencias.heading("cliente", text="CLIENTE", anchor="center")
    treeview_pendencias.heading("data_ocorrencia", text="DATA OCORRÊNCIA", anchor="center")
    treeview_pendencias.heading("razao_social", text="RAZÃO SOCIAL", anchor="center")
    treeview_pendencias.heading("cidade", text="CIDADE", anchor="center")
    treeview_pendencias.heading("vendedor", text="VENDEDOR", anchor="center")
    treeview_pendencias.heading("codigo_produto", text="CODIGO PRODUTO", anchor="center")
    treeview_pendencias.heading("quantidade", text="QUANTIDADE", anchor="center")

    treeview_pendencias.column("cupom", width=60, anchor="center")
    treeview_pendencias.column("cliente", width=128, anchor="center")
    treeview_pendencias.column("data_ocorrencia", width=128, anchor="center")
    treeview_pendencias.column("razao_social", width=128, anchor="center")
    treeview_pendencias.column("cidade", width=128, anchor="center")
    treeview_pendencias.column("vendedor", width=128, anchor="center")
    treeview_pendencias.column("codigo_produto", width=128, anchor="center")
    treeview_pendencias.column("quantidade", width=128, anchor="center")
    # endregion



    linha_horizontal_inferior = tk.Frame(janela_historico_pendencias, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)
