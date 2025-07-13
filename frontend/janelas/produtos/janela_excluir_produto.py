import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.produtos import (
    UNIDADE_MEDIDA_PRODUTOS,
    GRUPO_PRODUTOS,
    CATEGORIAS_PRODUTOS,
    MARCAS_PRODUTOS
)

from backend.binds.configuracao_binds import configurar_binds

from backend.validadores.produtos.formulario_produto import validar_formulario_produto

from backend.controladores.produto.excluir_controlador import limpar_entradas_excluir_produto
from backend.controladores.produto.excluir_controlador import excluir_produto_back
from backend.controladores.produto.excluir_controlador import buscar_produto_back


botao_buscar_apertado = False

def criar_janela_excluir_produto():

    def buscar_produto_gui():

        global botao_buscar_apertado

        codigo_produto = entry_codigo_produto_excluir

        valido, resposta = buscar_produto_back(codigo_produto.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            codigo_produto.focus_set()
            return None
        
        entry_descricao_excluir.insert(0, resposta[1])
        entry_subdescricao_excluir.insert(0, resposta[2])
        entry_unidade_medida_excluir.insert(0, resposta[4])
        entry_itens_embalagem_produtos_excluir.insert(0, resposta[5])
        entry_codigo_barras_excluir.insert(0, resposta[6])
        entry_grupo_produtos_excluir.insert(0, resposta[7])
        entry_categorias_produtos_excluir.insert(0, resposta[8])
        entry_marca_produtos_excluir.insert(0, resposta[9])
        entry_itens_pallete_excluir.insert(0, resposta[10])
        entry_itens_lastro_excluir.insert(0, resposta[11])

        botao_buscar_apertado = True

    def excluir_produto_gui():

        global botao_buscar_apertado

        codigo_produto = entry_codigo_produto_excluir
        descricao = entry_descricao_excluir
        subdescricao = entry_subdescricao_excluir
        unidade_medida = entry_unidade_medida_excluir
        itens_embalagem = entry_itens_embalagem_produtos_excluir
        codigo_barras = entry_codigo_barras_excluir
        grupo = entry_grupo_produtos_excluir
        categoria = entry_categorias_produtos_excluir
        marca = entry_marca_produtos_excluir
        itens_pallete = entry_itens_pallete_excluir
        itens_lastro = entry_itens_lastro_excluir

        valido, mensagem = validar_formulario_produto(
            codigo_produto,
            descricao,
            subdescricao,
            unidade_medida,
            itens_embalagem,
            codigo_barras,
            grupo,
            categoria,
            marca,
            itens_pallete,
            itens_lastro
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_produto_excluir.focus_set()
            return None

        if not botao_buscar_apertado:
            messagebox.showerror("Erro", "Busque o Produto Primeiro.")
            entry_codigo_produto_excluir.focus_set()
            return None
        
        excluir_produto_back(codigo_produto)

        
        limpar_entradas_excluir_produto([
            codigo_produto,
            descricao,
            subdescricao,
            unidade_medida,
            itens_embalagem,
            codigo_barras,
            grupo,
            categoria,
            marca,
            itens_pallete,
            itens_lastro
        ])        

        botao_buscar_apertado = False
        



    janela_excluir_produtos = tk.Toplevel()
    janela_excluir_produtos.title("Excluir Produto")
    janela_excluir_produtos.geometry("800x600")
    
    linha_horizontal_superior = tk.Frame(janela_excluir_produtos, background="silver", height=5, width=800)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_produto_excluir = tk.Label(janela_excluir_produtos, text="Código:", font=("Arial", 10, "bold"))
    label_codigo_produto_excluir.place(x=52, y=10)

    entry_codigo_produto_excluir = tk.Entry(janela_excluir_produtos, width=7, font=("Arial", 10))
    entry_codigo_produto_excluir.place(x=110, y=10)

    botao_buscar_produto_excluir = tk.Button(janela_excluir_produtos, text="Buscar", font=("Arial", 10, "bold"), command=buscar_produto_gui)
    botao_buscar_produto_excluir.place(x=170, y=6)

    label_descricao_excluir = tk.Label(janela_excluir_produtos, text="Descrição:", font=("Arial", 10, "bold"))
    label_descricao_excluir.place(x=35, y=40)

    entry_descricao_excluir = tk.Entry(janela_excluir_produtos, width=50, font=("Arial", 10))
    entry_descricao_excluir.place(x=110, y=40)

    label_produto_ativo_excluir = tk.Label(janela_excluir_produtos, text="Produto Ativo:", font=("Arial", 10, "bold"))
    label_produto_ativo_excluir.place(x=655, y=40)

    produto_ativo = tk.BooleanVar()
    entry_produto_ativo_excluir = tk.Checkbutton(janela_excluir_produtos, variable=produto_ativo)
    entry_produto_ativo_excluir.place(x=750, y=40)

    label_unidade_medida_excluir = tk.Label(janela_excluir_produtos, text="Unidade:", font=("Arial", 10, "bold"))
    label_unidade_medida_excluir.place(x=45, y=100)

    entry_unidade_medida_excluir = ttk.Combobox(janela_excluir_produtos, width=25, font=("Arial", 9, "bold"))
    entry_unidade_medida_excluir['values'] = UNIDADE_MEDIDA_PRODUTOS
    entry_unidade_medida_excluir.place(x=110, y=100)

    label_itens_embalagem_produtos_excluir = tk.Label(janela_excluir_produtos, text="Itens Embalagem:", font=("Arial", 10, "bold"))
    label_itens_embalagem_produtos_excluir.place(x=500, y=100)

    entry_itens_embalagem_produtos_excluir = tk.Entry(janela_excluir_produtos, font=("Arial", 10, "bold"))
    entry_itens_embalagem_produtos_excluir.place(x=625, y=100)

    label_subdescricao_excluir = tk.Label(janela_excluir_produtos, text="Subdescrição:", font=("Arial", 10, "bold"))
    label_subdescricao_excluir.place(x=10, y=150)

    entry_subdescricao_excluir = tk.Entry(janela_excluir_produtos, width=50, font=("Arial", 10, "bold"))
    entry_subdescricao_excluir.place(x=110, y=150)

    label_codigo_barras_excluir = tk.Label(janela_excluir_produtos, text="Código Barras:", font=("Arial", 10, "bold"))
    label_codigo_barras_excluir.place(x=520, y=150)

    entry_codigo_barras_excluir = tk.Entry(janela_excluir_produtos, font=("Arial", 10, "bold"))
    entry_codigo_barras_excluir.place(x=625, y=150)

    label_itens_pallete_excluir = tk.Label(janela_excluir_produtos, text="Itens Pallete:", font=("Arial", 10, "bold"))
    label_itens_pallete_excluir.place(x=530, y=200)

    entry_itens_pallete_excluir = tk.Entry(janela_excluir_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_pallete_excluir.place(x=625, y=200)

    label_itens_lastro_excluir = tk.Label(janela_excluir_produtos, width=9, text="Itens Lastro:", font=("Arial", 10, "bold"))
    label_itens_lastro_excluir.place(x=537, y=230)

    entry_itens_lastro_excluir = tk.Entry(janela_excluir_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_lastro_excluir.place(x=625, y=230)

    label_grupo_produtos_excluir = tk.Label(janela_excluir_produtos, text="Grupo:", font=("Arial", 10, "bold"))
    label_grupo_produtos_excluir.place(x=55, y=200)

    entry_grupo_produtos_excluir = ttk.Combobox(janela_excluir_produtos, width=25, font=("Arial", 9))
    entry_grupo_produtos_excluir["values"] = GRUPO_PRODUTOS
    entry_grupo_produtos_excluir.place(x=110, y=200)

    label_categorias_produtos_excluir = tk.Label(janela_excluir_produtos, text="Categoria:", font=("Arial", 10, "bold"))
    label_categorias_produtos_excluir.place(x=30, y=230)

    entry_categorias_produtos_excluir = ttk.Combobox(janela_excluir_produtos, width=25, font=("Arial", 9))
    entry_categorias_produtos_excluir["values"] = CATEGORIAS_PRODUTOS
    entry_categorias_produtos_excluir.place(x=110, y=230)

    label_marca_produtos_excluir = ttk.Label(janela_excluir_produtos, text="Marca:", font=("Arial", 10, "bold"))
    label_marca_produtos_excluir.place(x=55, y=260)

    entry_marca_produtos_excluir = ttk.Combobox(janela_excluir_produtos, width=25, font=("Arial", 9))
    entry_marca_produtos_excluir["values"] = MARCAS_PRODUTOS
    entry_marca_produtos_excluir.place(x=110, y=260)

    linha_horizontal_inferior = tk.Frame(janela_excluir_produtos, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_excluir = tk.Button(janela_excluir_produtos, text="Confirmar", font=("Arial", 10, "bold"), command=excluir_produto_gui)
    botao_confirmar_excluir.place(x=600, y=565)

    botao_cancelar_excluir = tk.Button(janela_excluir_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_excluir.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_produto_excluir,
        botao_buscar_produto_excluir,
        entry_descricao_excluir,
        entry_unidade_medida_excluir,
        entry_itens_embalagem_produtos_excluir,
        entry_subdescricao_excluir,
        entry_codigo_barras_excluir,
        entry_grupo_produtos_excluir,
        entry_categorias_produtos_excluir,
        entry_marca_produtos_excluir,
        entry_itens_pallete_excluir,
        entry_itens_lastro_excluir,
        botao_confirmar_excluir
    ]

    acoes_intermediarias = [None, buscar_produto_gui, None, None, None, None, None, None, None, None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias=acoes_intermediarias, ultima_acao=excluir_produto_gui)
