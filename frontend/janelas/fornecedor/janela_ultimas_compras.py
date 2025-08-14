import tkinter as tk
from tkinter import messagebox, ttk

from backend.binds.configuracao_binds import configurar_binds

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

def criar_janela_ultimas_compras():

    janela_ultimas_compras = tk.Toplevel()
    janela_ultimas_compras.geometry("800x600")
    janela_ultimas_compras.title("Últimas Compras")

    linha_horizontal_superior = tk.Frame(janela_ultimas_compras, background="silver", width=800, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_excluir = tk.Label(janela_ultimas_compras, text="Código:", font=LABEL)
    label_codigo_excluir.place(x=58, y=10)

    entry_codigo_excluir = tk.Entry(janela_ultimas_compras, width=7 ,font=ENTRY)
    entry_codigo_excluir.place(x=115, y=10)

    botao_buscar_excluir = tk.Button(janela_ultimas_compras, text="Buscar", font=BOTAO)
    botao_buscar_excluir.place(x=175, y=5)

    label_razao_social = tk.Label(janela_ultimas_compras, text="Razão Social:", font=LABEL)
    label_razao_social.place(x=20, y=40)

    entry_razao_social = tk.Entry(janela_ultimas_compras, font=ENTRY, width=60)
    entry_razao_social.place(x=115, y=40)

    scrollbar_vertical = ttk.Scrollbar(janela_ultimas_compras, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("data_ultima_compra", "numero_nota_fiscal")
    treeview_ultimas_compras = ttk.Treeview(
        janela_ultimas_compras,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_ultimas_compras.place(x=26, y=110, width=748, height=270)

    scrollbar_vertical.config(command=treeview_ultimas_compras.yview)

    treeview_ultimas_compras.heading("data_ultima_compra", text="DATA ÚLTIMA COMPRA", anchor="center")
    treeview_ultimas_compras.heading("numero_nota_fiscal", text="Nº NOTA FISCAL", anchor="center")

    treeview_ultimas_compras.column("data_ultima_compra", anchor="center")
    treeview_ultimas_compras.column("numero_nota_fiscal", anchor="center")



    linha_horizontal_inferior = tk.Frame(janela_ultimas_compras, background="silver", width=800, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_excluir = tk.Button(janela_ultimas_compras, text="Confirmar", font=BOTAO)
    botao_confirmar_excluir.place(x=600, y=565)

    botao_cancelar_excluir =  tk.Button(janela_ultimas_compras, text="Cancelar", font=BOTAO)
    botao_cancelar_excluir.place(x=700, y=565)