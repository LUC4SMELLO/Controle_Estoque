import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.produtos import (
    UNIDADE_MEDIDA_PRODUTOS,
    GRUPO_PRODUTOS,
    CATEGORIAS_PRODUTOS,
    MARCAS_PRODUTOS
)

from backend.validadores.produtos.formulario_produto import validar_formulario_produto

from backend.controladores.produto.alterar_controlador import alterar_produto_back
from backend.controladores.produto.consultar_controlador import buscar_produto_back

from backend.binds.configuracao_binds import configurar_binds


def criar_janela_alterar_produto():

    def buscar_produto_alterar_gui():

        global botao_buscar_apertado

        codigo_produto = entry_codigo_produto_alterar

        entry_descricao_alterar.delete(0, tk.END)
        entry_subdescricao_alterar.delete(0, tk.END)
        produto_ativo.set(False)
        entry_unidade_medida_alterar.delete(0, tk.END)
        entry_itens_embalagem_produtos_alterar.delete(0, tk.END)
        entry_codigo_barras_alterar.delete(0, tk.END)
        entry_grupo_produtos_alterar.delete(0, tk.END)
        entry_categorias_produtos_alterar.delete(0, tk.END)
        entry_marca_produtos_alterar.delete(0, tk.END)
        entry_itens_pallete_alterar.delete(0, tk.END)
        entry_itens_lastro_alterar.delete(0, tk.END)

        valido, resposta = buscar_produto_back(codigo_produto.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            codigo_produto.focus_set()
            return None
        
        entry_descricao_alterar.insert(0, resposta[1])
        entry_subdescricao_alterar.insert(0, resposta[2])
        produto_ativo.set(resposta[3])
        entry_unidade_medida_alterar.insert(0, resposta[4])
        entry_itens_embalagem_produtos_alterar.insert(0, resposta[5])
        entry_codigo_barras_alterar.insert(0, resposta[6])
        entry_grupo_produtos_alterar.insert(0, resposta[7])
        entry_categorias_produtos_alterar.insert(0, resposta[8])
        entry_marca_produtos_alterar.insert(0, resposta[9])
        entry_itens_pallete_alterar.insert(0, resposta[10])
        entry_itens_lastro_alterar.insert(0, resposta[11])

        botao_buscar_apertado = True
        

    def alterar_produto_gui():

        valido, mensagem = validar_formulario_produto(
            entry_codigo_produto_alterar.get(),
            entry_descricao_alterar.get(),
            entry_subdescricao_alterar.get(),
            entry_unidade_medida_alterar.get(),
            entry_itens_embalagem_produtos_alterar.get(),
            entry_codigo_barras_alterar.get(),
            entry_grupo_produtos_alterar.get(),
            entry_categorias_produtos_alterar.get(),
            entry_marca_produtos_alterar.get(),
            entry_itens_pallete_alterar.get(),
            entry_itens_lastro_alterar.get()    
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_produto_alterar.focus_set()
            return None

        alterar_produto_back(
        entry_codigo_produto_alterar,
        entry_descricao_alterar,
        entry_subdescricao_alterar,
        produto_ativo,
        entry_unidade_medida_alterar,
        entry_itens_embalagem_produtos_alterar,
        entry_codigo_barras_alterar,
        entry_grupo_produtos_alterar,
        entry_categorias_produtos_alterar,
        entry_marca_produtos_alterar,
        entry_itens_pallete_alterar,
        entry_itens_lastro_alterar,
    )   
        entry_codigo_produto_alterar.delete(0, tk.END)
        entry_descricao_alterar.delete(0, tk.END)
        entry_subdescricao_alterar.delete(0, tk.END)
        entry_unidade_medida_alterar.delete(0, tk.END)
        entry_itens_embalagem_produtos_alterar.delete(0, tk.END)
        entry_codigo_barras_alterar.delete(0, tk.END)
        entry_grupo_produtos_alterar.delete(0, tk.END)
        entry_categorias_produtos_alterar.delete(0, tk.END)
        entry_marca_produtos_alterar.delete(0, tk.END)
        entry_itens_pallete_alterar.delete(0, tk.END)
        entry_itens_lastro_alterar.delete(0, tk.END)

    janela_alterar_produtos = tk.Toplevel()
    janela_alterar_produtos.title("Alterar Produto")
    janela_alterar_produtos.geometry("800x600")
    
    linha_horizontal_superior = tk.Frame(janela_alterar_produtos, background="silver", height=5, width=800)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_produto_alterar = tk.Label(janela_alterar_produtos, text="Código:", font=("Arial", 10, "bold"))
    label_codigo_produto_alterar.place(x=52, y=10)

    entry_codigo_produto_alterar = tk.Entry(janela_alterar_produtos, width=7, font=("Arial", 10))
    entry_codigo_produto_alterar.place(x=110, y=10)

    botao_buscar_produto_alterar = tk.Button(janela_alterar_produtos, text="Buscar", font=("Arial", 10, "bold"), command=buscar_produto_alterar_gui)
    botao_buscar_produto_alterar.place(x=170, y=6)

    label_descricao_alterar = tk.Label(janela_alterar_produtos, text="Descrição:", font=("Arial", 10, "bold"))
    label_descricao_alterar.place(x=35, y=40)

    entry_descricao_alterar = tk.Entry(janela_alterar_produtos, width=50, font=("Arial", 10))
    entry_descricao_alterar.place(x=110, y=40)

    label_produto_ativo_alterar = tk.Label(janela_alterar_produtos, text="Produto Ativo:", font=("Arial", 10, "bold"))
    label_produto_ativo_alterar.place(x=655, y=40)

    produto_ativo = tk.BooleanVar()
    entry_produto_ativo_alterar = tk.Checkbutton(janela_alterar_produtos, variable=produto_ativo)
    entry_produto_ativo_alterar.place(x=750, y=40)

    label_unidade_medida_alterar = tk.Label(janela_alterar_produtos, text="Unidade:", font=("Arial", 10, "bold"))
    label_unidade_medida_alterar.place(x=45, y=100)

    entry_unidade_medida_alterar = ttk.Combobox(janela_alterar_produtos, width=25, font=("Arial", 9, "bold"))
    entry_unidade_medida_alterar['values'] = UNIDADE_MEDIDA_PRODUTOS
    entry_unidade_medida_alterar.place(x=110, y=100)

    label_itens_embalagem_produtos_alterar = tk.Label(janela_alterar_produtos, text="Itens Embalagem:", font=("Arial", 10, "bold"))
    label_itens_embalagem_produtos_alterar.place(x=500, y=100)

    entry_itens_embalagem_produtos_alterar = tk.Entry(janela_alterar_produtos, font=("Arial", 10, "bold"))
    entry_itens_embalagem_produtos_alterar.place(x=625, y=100)

    label_subdescricao_alterar = tk.Label(janela_alterar_produtos, text="Subdescrição:", font=("Arial", 10, "bold"))
    label_subdescricao_alterar.place(x=10, y=150)

    entry_subdescricao_alterar = tk.Entry(janela_alterar_produtos, width=50, font=("Arial", 10, "bold"))
    entry_subdescricao_alterar.place(x=110, y=150)

    label_codigo_barras_alterar = tk.Label(janela_alterar_produtos, text="Código Barras:", font=("Arial", 10, "bold"))
    label_codigo_barras_alterar.place(x=520, y=150)

    entry_codigo_barras_alterar = tk.Entry(janela_alterar_produtos, font=("Arial", 10, "bold"))
    entry_codigo_barras_alterar.place(x=625, y=150)

    label_itens_pallete_alterar = tk.Label(janela_alterar_produtos, text="Itens Pallete:", font=("Arial", 10, "bold"))
    label_itens_pallete_alterar.place(x=530, y=200)

    entry_itens_pallete_alterar = tk.Entry(janela_alterar_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_pallete_alterar.place(x=625, y=200)

    label_itens_lastro_alterar = tk.Label(janela_alterar_produtos, width=9, text="Itens Lastro:", font=("Arial", 10, "bold"))
    label_itens_lastro_alterar.place(x=537, y=230)

    entry_itens_lastro_alterar = tk.Entry(janela_alterar_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_lastro_alterar.place(x=625, y=230)

    label_grupo_produtos_alterar = tk.Label(janela_alterar_produtos, text="Grupo:", font=("Arial", 10, "bold"))
    label_grupo_produtos_alterar.place(x=55, y=200)

    entry_grupo_produtos_alterar = ttk.Combobox(janela_alterar_produtos, width=25, font=("Arial", 9))
    entry_grupo_produtos_alterar["values"] = GRUPO_PRODUTOS
    entry_grupo_produtos_alterar.place(x=110, y=200)

    label_categorias_produtos_alterar = tk.Label(janela_alterar_produtos, text="Categoria:", font=("Arial", 10, "bold"))
    label_categorias_produtos_alterar.place(x=30, y=230)

    entry_categorias_produtos_alterar = ttk.Combobox(janela_alterar_produtos, width=25, font=("Arial", 9))
    entry_categorias_produtos_alterar["values"] = CATEGORIAS_PRODUTOS
    entry_categorias_produtos_alterar.place(x=110, y=230)

    label_marca_produtos_alterar = ttk.Label(janela_alterar_produtos, text="Marca:", font=("Arial", 10, "bold"))
    label_marca_produtos_alterar.place(x=55, y=260)

    entry_marca_produtos_alterar = ttk.Combobox(janela_alterar_produtos, width=25, font=("Arial", 9))
    entry_marca_produtos_alterar["values"] = MARCAS_PRODUTOS
    entry_marca_produtos_alterar.place(x=110, y=260)

    linha_horizontal_inferior = tk.Frame(janela_alterar_produtos, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_alterar = tk.Button(janela_alterar_produtos, text="Confirmar", font=("Arial", 10, "bold"), command=alterar_produto_gui)
    botao_confirmar_alterar.place(x=600, y=565)

    botao_cancelar_alterar = tk.Button(janela_alterar_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_alterar.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_produto_alterar,
        botao_buscar_produto_alterar,
        entry_descricao_alterar,
        entry_unidade_medida_alterar,
        entry_itens_embalagem_produtos_alterar,
        entry_subdescricao_alterar,
        entry_codigo_barras_alterar,
        entry_grupo_produtos_alterar,
        entry_categorias_produtos_alterar,
        entry_marca_produtos_alterar,
        entry_itens_pallete_alterar,
        entry_itens_lastro_alterar,
        botao_confirmar_alterar
    ]

    acoes_intermediarias = [None, buscar_produto_alterar_gui, None, None, None, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias=acoes_intermediarias, ultima_acao=alterar_produto_gui)
