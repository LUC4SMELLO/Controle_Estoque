import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.produtos import (
    UNIDADE_MEDIDA_PRODUTOS,
    GRUPO_PRODUTOS,
    CATEGORIAS_PRODUTOS,
    MARCAS_PRODUTOS
)

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.controladores.produto.consultar_controlador import buscar_produto_back

from backend.binds.configuracao_binds import configurar_binds


def criar_janela_consultar_produto():

    def consultar_produto_gui():

        codigo_produto = entry_codigo_produto_consultar

        entry_descricao_consultar.delete(0, tk.END)
        entry_subdescricao_consultar.delete(0, tk.END)
        produto_ativo.set(False)
        entry_unidade_medida_consultar.delete(0, tk.END)
        entry_itens_embalagem_produtos_consultar.delete(0, tk.END)
        entry_codigo_barras_consultar.delete(0, tk.END)
        entry_grupo_produtos_consultar.delete(0, tk.END)
        entry_categorias_produtos_consultar.delete(0, tk.END)
        entry_marca_produtos_consultar.delete(0, tk.END)
        entry_itens_pallete_consultar.delete(0, tk.END)
        entry_itens_lastro_consultar.delete(0, tk.END)
        entry_estoque_consultar.delete(0, tk.END)
        
        valido, resposta = buscar_produto_back(codigo_produto.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            codigo_produto.focus_set()
            return None
        
        
        entry_descricao_consultar.insert(0, resposta.descricao)
        entry_subdescricao_consultar.insert(0, resposta.subdescricao)
        produto_ativo.set(resposta.produto_ativo)
        entry_unidade_medida_consultar.insert(0, resposta.unidade_medida)
        entry_itens_embalagem_produtos_consultar.insert(0, resposta.itens_embalagem)
        entry_codigo_barras_consultar.insert(0, resposta.codigo_barras)
        entry_grupo_produtos_consultar.insert(0, resposta.grupo)
        entry_categorias_produtos_consultar.insert(0, resposta.categoria)
        entry_marca_produtos_consultar.insert(0, resposta.marca)
        entry_itens_pallete_consultar.insert(0, resposta.itens_pallete)
        entry_itens_lastro_consultar.insert(0, resposta.itens_lastro)
        entry_estoque_consultar.insert(0, resposta.quantidade_estoque)

    def fechar_janela_consultar_produto():

        janela_consultar_produtos.destroy()

        
    janela_consultar_produtos = tk.Toplevel()
    janela_consultar_produtos.title("Consultar Produto")
    janela_consultar_produtos.geometry("800x600")
    
    linha_horizontal_superior = tk.Frame(janela_consultar_produtos, background="silver", height=5, width=800)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_produto_consultar = tk.Label(janela_consultar_produtos, text="Código:", font=LABEL)
    label_codigo_produto_consultar.place(x=52, y=10)

    entry_codigo_produto_consultar = tk.Entry(janela_consultar_produtos, width=7, font=ENTRY)
    entry_codigo_produto_consultar.place(x=110, y=10)

    botao_buscar_produto_consultar = tk.Button(janela_consultar_produtos, text="Buscar", font=BOTAO, command=consultar_produto_gui)
    botao_buscar_produto_consultar.place(x=170, y=6)

    label_descricao_consultar = tk.Label(janela_consultar_produtos, text="Descrição:", font=LABEL)
    label_descricao_consultar.place(x=35, y=40)

    entry_descricao_consultar = tk.Entry(janela_consultar_produtos, width=50, font=ENTRY)
    entry_descricao_consultar.place(x=110, y=40)

    label_produto_ativo_consultar = tk.Label(janela_consultar_produtos, text="Produto Ativo:", font=LABEL)
    label_produto_ativo_consultar.place(x=655, y=40)

    produto_ativo = tk.BooleanVar()
    entry_produto_ativo_consultar = tk.Checkbutton(janela_consultar_produtos, variable=produto_ativo)
    entry_produto_ativo_consultar.place(x=750, y=40)

    label_unidade_medida_consultar = tk.Label(janela_consultar_produtos, text="Unidade:", font=LABEL)
    label_unidade_medida_consultar.place(x=45, y=100)

    entry_unidade_medida_consultar = ttk.Combobox(janela_consultar_produtos, width=25, font=ENTRY)
    entry_unidade_medida_consultar['values'] = UNIDADE_MEDIDA_PRODUTOS
    entry_unidade_medida_consultar.place(x=110, y=100)

    label_itens_embalagem_produtos_consultar = tk.Label(janela_consultar_produtos, text="Itens Embalagem:", font=LABEL)
    label_itens_embalagem_produtos_consultar.place(x=500, y=100)

    entry_itens_embalagem_produtos_consultar = tk.Entry(janela_consultar_produtos, font=ENTRY)
    entry_itens_embalagem_produtos_consultar.place(x=625, y=100)

    label_subdescricao_consultar = tk.Label(janela_consultar_produtos, text="Subdescrição:", font=LABEL)
    label_subdescricao_consultar.place(x=10, y=150)

    entry_subdescricao_consultar = tk.Entry(janela_consultar_produtos, width=50, font=ENTRY)
    entry_subdescricao_consultar.place(x=110, y=150)

    label_codigo_barras_consultar = tk.Label(janela_consultar_produtos, text="Código Barras:", font=LABEL)
    label_codigo_barras_consultar.place(x=520, y=150)

    entry_codigo_barras_consultar = tk.Entry(janela_consultar_produtos, font=ENTRY)
    entry_codigo_barras_consultar.place(x=625, y=150)

    label_itens_pallete_consultar = tk.Label(janela_consultar_produtos, text="Itens Pallete:", font=LABEL)
    label_itens_pallete_consultar.place(x=530, y=200)

    entry_itens_pallete_consultar = tk.Entry(janela_consultar_produtos, width=9, font=ENTRY)
    entry_itens_pallete_consultar.place(x=625, y=200)

    label_itens_lastro_consultar = tk.Label(janela_consultar_produtos, width=9, text="Itens Lastro:", font=LABEL)
    label_itens_lastro_consultar.place(x=537, y=230)

    entry_itens_lastro_consultar = tk.Entry(janela_consultar_produtos, width=9, font=ENTRY)
    entry_itens_lastro_consultar.place(x=625, y=230)

    label_grupo_produtos_consultar = tk.Label(janela_consultar_produtos, text="Grupo:", font=LABEL)
    label_grupo_produtos_consultar.place(x=55, y=200)

    entry_grupo_produtos_consultar = ttk.Combobox(janela_consultar_produtos, width=25, font=ENTRY)
    entry_grupo_produtos_consultar["values"] = GRUPO_PRODUTOS
    entry_grupo_produtos_consultar.place(x=110, y=200)

    label_categorias_produtos_consultar = tk.Label(janela_consultar_produtos, text="Categoria:", font=LABEL)
    label_categorias_produtos_consultar.place(x=30, y=230)

    entry_categorias_produtos_consultar = ttk.Combobox(janela_consultar_produtos, width=25, font=ENTRY)
    entry_categorias_produtos_consultar["values"] = CATEGORIAS_PRODUTOS
    entry_categorias_produtos_consultar.place(x=110, y=230)

    label_marca_produtos_consultar = ttk.Label(janela_consultar_produtos, text="Marca:", font=LABEL)
    label_marca_produtos_consultar.place(x=55, y=260)

    entry_marca_produtos_consultar = ttk.Combobox(janela_consultar_produtos, width=25, font=ENTRY)
    entry_marca_produtos_consultar["values"] = MARCAS_PRODUTOS
    entry_marca_produtos_consultar.place(x=110, y=260)

    label_estoque_consultar = tk.Label(janela_consultar_produtos, text="Estoque:", font=LABEL)
    label_estoque_consultar.place(x=558, y=260)

    entry_estoque_consultar = tk.Entry(janela_consultar_produtos, width=9, font=ENTRY)
    entry_estoque_consultar.place(x=625, y=260)

    linha_horizontal_inferior = tk.Frame(janela_consultar_produtos, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_consultar = tk.Button(janela_consultar_produtos, text="Confirmar", font=BOTAO)
    botao_confirmar_consultar.place(x=600, y=565)

    botao_cancelar_consultar = tk.Button(janela_consultar_produtos, text="Cancelar", font=BOTAO, command=fechar_janela_consultar_produto)
    botao_cancelar_consultar.place(x=700, y=565)


    lista_entrys = [
        entry_codigo_produto_consultar,
        botao_buscar_produto_consultar,
        entry_descricao_consultar,
        entry_unidade_medida_consultar,
        entry_itens_embalagem_produtos_consultar,
        entry_subdescricao_consultar,
        entry_codigo_barras_consultar,
        entry_grupo_produtos_consultar,
        entry_categorias_produtos_consultar,
        entry_marca_produtos_consultar,
        entry_itens_pallete_consultar,
        entry_itens_lastro_consultar,
        botao_confirmar_consultar
    ]

    acoes_intermediarias = [None, consultar_produto_gui, None, None, None, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, None)
    