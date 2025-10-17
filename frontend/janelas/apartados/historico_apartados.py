import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds


def criar_janela_historico_apartados():

    def buscar_apartados_gui():
        pass


    janela_historico_apartar = tk.Toplevel()
    janela_historico_apartar.title("Histórico Apartados")
    janela_historico_apartar.geometry("1100x600")
    janela_historico_apartar.resizable(False, False)


    label_data = tk.Label(janela_historico_apartar, text="Data:", font=LABEL)
    label_data.place(x=20, y=20)

    entry_data = tk.Entry(janela_historico_apartar, width=10, font=ENTRY)
    entry_data.place(x=60, y=20)

    label_codigo_produto = tk.Label(janela_historico_apartar, text="Código Produto:", font=LABEL)
    label_codigo_produto.place(x=150, y=20)

    entry_codigo_produto = tk.Entry(janela_historico_apartar, width=10, font=ENTRY)
    entry_codigo_produto.place(x=260, y=20)


    botao_buscar_apartados = tk.Button(janela_historico_apartar, text="Buscar", font=BOTAO, command=buscar_apartados_gui)
    botao_buscar_apartados.place(x=345, y=17)


    linha_horizontal_superior = tk.Frame(janela_historico_apartar, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)




    scrollbar_vertical = ttk.Scrollbar(janela_historico_apartar, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("data", "codigo_produto", "descricao", "quantidade", "motivo")
    treeview_nota_fiscal = ttk.Treeview(
        janela_historico_apartar,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_nota_fiscal.place(x=20, y=110, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_nota_fiscal.yview)

    treeview_nota_fiscal.heading("data", text="DATA", anchor="center")
    treeview_nota_fiscal.heading("codigo_produto", text="CÓDIGO PRODUTO", anchor="center")
    treeview_nota_fiscal.heading("descricao", text="DESCRIÇÃO", anchor="center")
    treeview_nota_fiscal.heading("quantidade", text="QUANTIDADE", anchor="center")
    treeview_nota_fiscal.heading("motivo", text="MOTIVO", anchor="center")

    treeview_nota_fiscal.column("data", width=120, anchor="center")
    treeview_nota_fiscal.column("codigo_produto", width=160, anchor="center")
    treeview_nota_fiscal.column("descricao", width=220, anchor="center")
    treeview_nota_fiscal.column("quantidade", width=120, anchor="center")
    treeview_nota_fiscal.column("motivo", width=120, anchor="center")
    # endregion

    linha_horizontal_inferior = tk.Frame(janela_historico_apartar, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)




    lista_entrys = [entry_data, entry_codigo_produto, botao_buscar_apartados]
    
    acoes_intermediarias = [None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias)
