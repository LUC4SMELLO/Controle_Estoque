import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controladores.estoque.entrada_nota_fiscal_controlador import (
    buscar_nota_fiscal_back,
    data_entrada_atual, 
    verificar_produtos_da_nota_fiscal,
    entrada_produto_nota_fiscal_back,
    buscar_fornecedor_pelo_cnpj_back,
    salvar_nota_fiscal_back,
    nota_fiscal_ja_importada,
    salvar_item_nota_fiscal_back
)   

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds 

resultados_nota_fiscal = None
resposta_fornecedor = None
produtos_listados_na_tabela = False

def criar_janela_entrada_nota_fiscal():

    data_entrada_agora = data_entrada_atual()

    def mostrar_nota_fiscal():

        global resultados_nota_fiscal
        global resposta_fornecedor
        global produtos_listados_na_tabela

        resultados_nota_fiscal = buscar_nota_fiscal_back() 

        valido, resposta_fornecedor = buscar_fornecedor_pelo_cnpj_back(resultados_nota_fiscal[0]["cnpj"])
        if not valido:
            messagebox.showerror("Erro", resposta_fornecedor)
            return None

        valido, resposta = verificar_produtos_da_nota_fiscal(resultados_nota_fiscal)
        if not valido:
            messagebox.showerror("Erro", f"Os Seguintes Produtos Não Foram Encontrados: \n\n{resposta}")
            treeview_nota_fiscal.focus_set()
            return None

        for item in treeview_nota_fiscal.get_children():
            treeview_nota_fiscal.delete(item)

        if not resultados_nota_fiscal:
            messagebox.showinfo("Aviso", "Não Há Produtos a Serem Listados ou um Erro Ocorreu na Leitura.")
            treeview_nota_fiscal.focus_set()
            return None
        
        resultado, _ = nota_fiscal_ja_importada(resultados_nota_fiscal[0]["numero_nota"])
        if not resultado:
            label_nota_importada.config(text="Nota Já Importada!", bg="Black", fg="Yellow")
 
        entry_data_entrada.delete(0, tk.END)
        entry_codigo_fornecedor.delete(0, tk.END)
        entry_numero_nota_fiscal.delete(0, tk.END)
        entry_descricao_fornecedor.delete(0, tk.END)
        entry_municipio.delete(0, tk.END)
        entry_uf.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)

        entry_data_entrada.insert(0, data_entrada_agora)
        entry_codigo_fornecedor.insert(0, resposta_fornecedor.codigo_fornecedor)
        entry_numero_nota_fiscal.insert(0, resultados_nota_fiscal[0]["numero_nota"])
        entry_descricao_fornecedor.insert(0, resultados_nota_fiscal[0]["razao_social"])
        entry_municipio.insert(0, (resultados_nota_fiscal[0]["cidade"]))
        entry_uf.insert(0, (resultados_nota_fiscal[0]["uf"]))
        entry_bairro.insert(0, resultados_nota_fiscal[0]["bairro"])
        
        numero_item = 1
        for produto_dict in resultados_nota_fiscal:

            valores_para_treeview = (
                numero_item,
                produto_dict.get("codigo_produto", ""),
                produto_dict.get("descricao", ""),
                produto_dict.get("quantidade", 0),
                produto_dict.get("preco_unitario", 0),
                produto_dict.get("preco_total", 0)
            )
            treeview_nota_fiscal.insert("", "end", values=valores_para_treeview)

            numero_item += 1

        produtos_listados_na_tabela = True

        messagebox.showinfo("Sucesso", f"{len(resultados_nota_fiscal)} Produtos Listados na Tabela.")
        treeview_nota_fiscal.focus_set()

    def entrada_produto_gui():

        global resultados_nota_fiscal
        global resposta_fornecedor
        global produtos_listados_na_tabela

        if not produtos_listados_na_tabela:
            messagebox.showerror("Erro.", "Busque uma Nota Fiscal Primeiro.")
            botao_buscar_nota_fiscal.focus_set()
            return None
        
        resultado, mensagem = salvar_nota_fiscal_back(
            resultados_nota_fiscal[0]["numero_nota"],
            resposta_fornecedor.codigo_fornecedor,
            data_entrada_agora
            )
        if not resultado:
            messagebox.showerror("Erro", mensagem)
            treeview_nota_fiscal.focus_set()
            return None
        
        for produto_dict in resultados_nota_fiscal:
            salvar_item_nota_fiscal_back(
                resultados_nota_fiscal[0]["numero_nota"],
                produto_dict.get("codigo_produto", ""),
                produto_dict.get("quantidade", 0),
                produto_dict.get("preco_unitario", 0),
                produto_dict.get("preco_total", 0)
            )
        
        entrada_produto_nota_fiscal_back(resultados_nota_fiscal)

        messagebox.showinfo("Sucesso!", "Nota Importada.")

        produtos_listados_na_tabela = False

        for item in treeview_nota_fiscal.get_children():
            treeview_nota_fiscal.delete(item)

        entry_data_entrada.delete(0, tk.END)
        entry_codigo_fornecedor.delete(0, tk.END)
        entry_numero_nota_fiscal.delete(0, tk.END)
        entry_descricao_fornecedor.delete(0, tk.END)
        entry_municipio.delete(0, tk.END)
        entry_uf.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)

        treeview_nota_fiscal.focus_set()

    def fechar_janela_entrada_produtos_nota_fiscal():
        
        global produtos_listados_na_tabela

        produtos_listados_na_tabela = False

        janela_entrada_nota_fiscal.destroy()


    janela_entrada_nota_fiscal = tk.Toplevel()
    janela_entrada_nota_fiscal.title("Entrada Nota Fiscal")
    janela_entrada_nota_fiscal.geometry("1100x600")

    label_data_entrada = tk.Label(janela_entrada_nota_fiscal, text="Data Entrada:", font=LABEL)
    label_data_entrada.place(x=26, y=10)

    entry_data_entrada = tk.Entry(janela_entrada_nota_fiscal, width=10, font=ENTRY)
    entry_data_entrada.place(x=120, y=10)

    label_fornecedor = tk.Label(janela_entrada_nota_fiscal, text="Fornecedor:", font=LABEL)
    label_fornecedor.place(x=200, y=10)

    entry_codigo_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=6, font=ENTRY)
    entry_codigo_fornecedor.place(x=285, y=10)

    entry_descricao_fornecedor = tk.Entry(janela_entrada_nota_fiscal, width=53, font=ENTRY)
    entry_descricao_fornecedor.place(x=335, y=10)

    label_uf = tk.Label(janela_entrada_nota_fiscal, text="UF:", font=LABEL)
    label_uf.place(x=256, y=40)

    entry_uf = tk.Entry(janela_entrada_nota_fiscal, width=6, font=ENTRY)
    entry_uf.place(x=285, y=40)

    label_municipio = tk.Label(janela_entrada_nota_fiscal, text="Município:", font=LABEL)
    label_municipio.place(x=332, y=40)

    entry_municipio = tk.Entry(janela_entrada_nota_fiscal, font=ENTRY)
    entry_municipio.place(x=405, y=40)

    label_bairro = tk.Label(janela_entrada_nota_fiscal, text="Bairro:", font=LABEL)
    label_bairro.place(x=515, y=40)

    label_nota_importada = tk.Label(janela_entrada_nota_fiscal, text="", font=LABEL)
    label_nota_importada.place(x=750, y=40)

    entry_bairro = tk.Entry(janela_entrada_nota_fiscal, font=ENTRY)
    entry_bairro.place(x=565, y=40)

    label_numero_nota_fiscal = tk.Label(janela_entrada_nota_fiscal, text="Número NF-e:", font=LABEL)
    label_numero_nota_fiscal.place(x=24, y=40)

    entry_numero_nota_fiscal = tk.Entry(janela_entrada_nota_fiscal, width=10, font=ENTRY)
    entry_numero_nota_fiscal.place(x=120, y=40)

    botao_buscar_nota_fiscal = tk.Button(janela_entrada_nota_fiscal, text="Buscar\nNota Fiscal", font=BOTAO, command=mostrar_nota_fiscal)
    botao_buscar_nota_fiscal.place(x=1000, y=10)

    linha_horizontal_superior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)

    scrollbar_vertical = ttk.Scrollbar(janela_entrada_nota_fiscal, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("numero_item", "codigo_produto", "descricao", "quantidade", "preco_unitario", "preco_total")
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
    treeview_nota_fiscal.heading("preco_unitario", text="PREÇO UNITÁRIO", anchor="center")
    treeview_nota_fiscal.heading("preco_total", text="PREÇO TOTAL", anchor="center")

    treeview_nota_fiscal.column("numero_item", width=120, anchor="center")
    treeview_nota_fiscal.column("codigo_produto", width=160, anchor="center")
    treeview_nota_fiscal.column("descricao", width=220, anchor="center")
    treeview_nota_fiscal.column("quantidade", width=120, anchor="center")
    treeview_nota_fiscal.column("preco_unitario", width=120, anchor="center")
    treeview_nota_fiscal.column("preco_total", width=120, anchor="center")
    # endregion

    linha_horizontal_inferior = tk.Frame(janela_entrada_nota_fiscal, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_entrada = tk.Button(janela_entrada_nota_fiscal, text="Confirmar", font=BOTAO, command=entrada_produto_gui)
    botao_confirmar_entrada.place(x=900, y=565)

    botao_cancelar_saida = tk.Button(janela_entrada_nota_fiscal, text="Cancelar", font=BOTAO, command=fechar_janela_entrada_produtos_nota_fiscal)
    botao_cancelar_saida.place(x=1000, y=565)

