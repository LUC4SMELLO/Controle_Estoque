import tkinter as tk
from tkinter import messagebox, ttk

from backend.binds.configuracao_binds import configurar_binds

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.controladores.fornecedor.ultimas_compras_controlador import retornar_ultimas_compras_fornecedor

from backend.controladores.fornecedor.consultar_fornecedor_controlador import buscar_fornecedor_back

def criar_janela_ultimas_compras():

    def buscar_fornecedor_gui():

        entry_razao_social.delete(0, tk.END)

        valido, resposta = buscar_fornecedor_back(entry_codigo_ultimas_compras.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            entry_codigo_ultimas_compras.focus_set()
            return None

        entry_razao_social.insert(0, resposta.razao_social)
    

    janela_ultimas_compras = tk.Toplevel()
    janela_ultimas_compras.geometry("1100x600")
    janela_ultimas_compras.title("Últimas Compras")

    linha_horizontal_superior = tk.Frame(janela_ultimas_compras, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_ultimas_compras = tk.Label(janela_ultimas_compras, text="Código:", font=LABEL)
    label_codigo_ultimas_compras.place(x=58, y=10)

    entry_codigo_ultimas_compras = tk.Entry(janela_ultimas_compras, width=7 ,font=ENTRY)
    entry_codigo_ultimas_compras.place(x=115, y=10)

    botao_buscar_ultimas_compras = tk.Button(janela_ultimas_compras, text="Buscar", font=BOTAO, command=buscar_fornecedor_gui)
    botao_buscar_ultimas_compras.place(x=175, y=5)

    label_razao_social = tk.Label(janela_ultimas_compras, text="Razão Social:", font=LABEL)
    label_razao_social.place(x=20, y=40)

    entry_razao_social = tk.Entry(janela_ultimas_compras, font=ENTRY, width=60)
    entry_razao_social.place(x=115, y=40)
    
    scrollbar_vertical = ttk.Scrollbar(janela_ultimas_compras, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("data_entrada", "numero_nota_fiscal", "codigo_produto", "descricao", "quantidade", "preco_unitario", "preco_total")
    treeview_ultimas_compras = ttk.Treeview(
        janela_ultimas_compras,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_ultimas_compras.place(x=26, y=110, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_ultimas_compras.yview)

    treeview_ultimas_compras.heading("data_entrada", text="DATA ENTRADA", anchor="center")
    treeview_ultimas_compras.heading("numero_nota_fiscal", text="NOTA FISCAL", anchor="center")
    treeview_ultimas_compras.heading("codigo_produto", text="CÓDIGO PRODUTO", anchor="center")
    treeview_ultimas_compras.heading("descricao", text="DESCRIÇÃO", anchor="center")
    treeview_ultimas_compras.heading("quantidade", text="QUANTIDADE", anchor="center")
    treeview_ultimas_compras.heading("preco_unitario", text="PREÇO UNITÁRIO", anchor="center")
    treeview_ultimas_compras.heading("preco_total", text="PREÇO TOTAL", anchor="center")

    treeview_ultimas_compras.column("data_entrada", width=120)
    treeview_ultimas_compras.column("numero_nota_fiscal", width=110, anchor="center")
    treeview_ultimas_compras.column("codigo_produto", width=120, anchor="center")
    treeview_ultimas_compras.column("descricao", width=260, anchor="center")
    treeview_ultimas_compras.column("quantidade", width=90, anchor="center")
    treeview_ultimas_compras.column("preco_unitario", width=120, anchor="center")
    treeview_ultimas_compras.column("preco_total", width=120, anchor="center")

    


    linha_horizontal_inferior = tk.Frame(janela_ultimas_compras, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_ultimas_compras = tk.Button(janela_ultimas_compras, text="Confirmar", font=BOTAO)
    botao_confirmar_ultimas_compras.place(x=900, y=565)

    botao_cancelar_ultimas_compras =  tk.Button(janela_ultimas_compras, text="Cancelar", font=BOTAO)
    botao_cancelar_ultimas_compras.place(x=1000, y=565)