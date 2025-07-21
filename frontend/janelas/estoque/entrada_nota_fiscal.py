import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controladores.estoque.entrada_nota_fiscal_controlador import buscar_nota_fiscal_back

from backend.controladores.estoque.entrada_controlador import entrada_produto_back

from backend.binds.configuracao_binds import configurar_binds 

def criar_janela_entrada_nota_fiscal():
    def mostrar_nota_fiscal():


        resultados = buscar_nota_fiscal_back() 

        for item in treeview_nota_fiscal.get_children():
            treeview_nota_fiscal.delete(item)

        if not resultados:
            messagebox.showinfo("Aviso", "Não há produtos a serem listados ou um erro ocorreu na leitura.")
            return None 
        
        for produto_dict in resultados:

            valores_para_treeview = (
                produto_dict.get("codigo", ""),
                produto_dict.get("descricao", ""),
                produto_dict.get("unidade", ""),
                produto_dict.get("quantidade", 0)
            )
            treeview_nota_fiscal.insert("", "end", values=valores_para_treeview)

        messagebox.showinfo("Sucesso", f"{len(resultados)} produtos listados na tabela.") 

    janela_entrada_nota_fiscal = tk.Toplevel()
    janela_entrada_nota_fiscal.title("Entrada Nota Fiscal")
    janela_entrada_nota_fiscal.geometry("1100x600")

    label_data_entrada = tk.Label(janela_entrada_nota_fiscal, text="Data Entrada:", font=("Arial", 10, "bold"))
    label_data_entrada.place(x=26, y=10)

    entry_data_entrada = tk.Entry(janela_entrada_nota_fiscal, width=10, font=("Arial", 10, "bold"))
    entry_data_entrada.place(x=120, y=10)

    label_fornecedor = tk.Label(janela_entrada_nota_fiscal, text="Fornecedor:", font=("Arial", 10, "bold"))
    label_fornecedor.place(x=200, y=10)

    entry_codigo_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=6, font=("Arial", 10, "bold"))
    entry_codigo_fornecedor.place(x=285, y=10)

    entry_descricao_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=53, font=("Arial", 10, "bold"))
    entry_descricao_fornecedor.place(x=335, y=10)

    label_uf = tk.Label(janela_entrada_nota_fiscal, text="UF:", font=("Arial", 10, "bold"))
    label_uf.place(x=256, y=40)

    entry_uf = tk.Entry(janela_entrada_nota_fiscal, width=6, font=("Arial", 10, "bold"))
    entry_uf.place(x=285, y=40)

    label_municipio = tk.Label(janela_entrada_nota_fiscal, text="Município:", font=("Arial", 10, "bold"))
    label_municipio.place(x=332, y=40)

    entry_municipio = tk.Entry(janela_entrada_nota_fiscal, font=("Arial", 10, "bold"))
    entry_municipio.place(x=405, y=40)

    label_bairro = tk.Label(janela_entrada_nota_fiscal, text="Bairro:", font=("Arial", 10, "bold"))
    label_bairro.place(x=515, y=40)

    entry_bairro = tk.Entry(janela_entrada_nota_fiscal, font=("Arial", 10, "bold"))
    entry_bairro.place(x=565, y=40)

    label_numero_nota_fiscal = tk.Label(janela_entrada_nota_fiscal, text="Número NF-e:", font=("Arial", 10, "bold"))
    label_numero_nota_fiscal.place(x=24, y=40)

    entry_numero_nota_fiscal = tk.Entry(janela_entrada_nota_fiscal, width=10, font=("Arial", 10, "bold"))
    entry_numero_nota_fiscal.place(x=120, y=40)

    botao_buscar_nota_fiscal = tk.Button(janela_entrada_nota_fiscal, text="Buscar\nNota Fiscal", font=("Arial", 10, "bold"), command=mostrar_nota_fiscal)
    botao_buscar_nota_fiscal.place(x=1000, y=10)

    linha_horizontal_superior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)

    scrollbar_vertical = ttk.Scrollbar(janela_entrada_nota_fiscal, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("numero_item", "codigo_produto", "descricao", "quantidade")
    treeview_nota_fiscal = ttk.Treeview(
        janela_entrada_nota_fiscal,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_nota_fiscal.place(x=26, y=110, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_nota_fiscal.yview)

    treeview_nota_fiscal.heading("numero_item", text="Nº ITEM", anchor="center")
    treeview_nota_fiscal.heading("codigo_produto", text="CÓDIGO PRODUTO", anchor="center")
    treeview_nota_fiscal.heading("descricao", text="DESCRIÇÃO", anchor="center")
    treeview_nota_fiscal.heading("quantidade", text="QUANTIDADE", anchor="center")

    treeview_nota_fiscal.column("numero_item", width=120, anchor="center")
    treeview_nota_fiscal.column("codigo_produto", width=160, anchor="center")
    treeview_nota_fiscal.column("descricao", width=220, anchor="center")
    treeview_nota_fiscal.column("quantidade", width=120, anchor="center")
    # endregion




    linha_horizontal_inferior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_entrada = tk.Button(janela_entrada_nota_fiscal, text="Confirmar", font=("Arial", 10, "bold"))
    botao_confirmar_entrada.place(x=900, y=565)

    botao_cancelar_saida = tk.Button(janela_entrada_nota_fiscal, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_saida.place(x=1000, y=565)

