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

from backend.controladores.produto.cadastrar_controlador import cadastrar_produto_back
from servicos.servico_produtos import produto_exite

from backend.binds.configuracao_binds import configurar_binds

def criar_janela_cadastrar_produto():

    def cadastrar_produto_gui():
        
        valido, mensagem = produto_exite(entry_codigo_produto_cadastrar.get().strip())
        if valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_produto_cadastrar.focus_set()
            return None
    
        valido, mensagem = validar_formulario_produto(
            entry_codigo_produto_cadastrar.get().strip(),
            entry_descricao_cadastrar.get().strip(),
            entry_subdescricao_cadastar.get().strip(),
            entry_unidade_medida_cadastrar.get().strip(),
            entry_itens_embalagem_produtos_cadastrar.get().strip(),
            entry_codigo_barras_cadastrar.get().strip(),
            entry_grupo_produtos_cadastrar.get().strip(),
            entry_categorias_produtos_cadastrar.get().strip(),
            entry_marca_produtos_cadastrar.get().strip(),
            entry_itens_pallete_cadastrar.get().strip(),
            entry_itens_lastro_cadastrar.get().strip()
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_codigo_produto_cadastrar.focus_set()
            return None

        cadastrar_produto_back(
            entry_codigo_produto_cadastrar,
            entry_descricao_cadastrar,
            entry_subdescricao_cadastar,
            produto_ativo,
            entry_unidade_medida_cadastrar,
            entry_itens_embalagem_produtos_cadastrar,
            entry_codigo_barras_cadastrar,
            entry_grupo_produtos_cadastrar,
            entry_categorias_produtos_cadastrar,
            entry_marca_produtos_cadastrar,
            entry_itens_pallete_cadastrar,
            entry_itens_lastro_cadastrar

        )
        

        limpar_entradas_cadastro_produto()

    def limpar_entradas_cadastro_produto():
        entry_codigo_produto_cadastrar.delete(0, tk.END)
        entry_descricao_cadastrar.delete(0, tk.END)
        entry_subdescricao_cadastar.delete(0, tk.END)
        produto_ativo.set(False)
        entry_unidade_medida_cadastrar.delete(0, tk.END)
        entry_itens_embalagem_produtos_cadastrar.delete(0, tk.END)
        entry_codigo_barras_cadastrar.delete(0, tk.END)
        entry_grupo_produtos_cadastrar.delete(0, tk.END)
        entry_categorias_produtos_cadastrar.delete(0, tk.END)
        entry_marca_produtos_cadastrar.delete(0, tk.END)
        entry_itens_pallete_cadastrar.delete(0, tk.END)
        entry_itens_lastro_cadastrar.delete(0, tk.END)



    janela_cadastrar_produtos = tk.Toplevel()
    janela_cadastrar_produtos.title("Cadastrar Produto")
    janela_cadastrar_produtos.geometry("800x600")
    
    linha_horizontal_superior = tk.Frame(janela_cadastrar_produtos, background="silver", height=5, width=800)
    linha_horizontal_superior.place(x=0, y=75)

    label_codigo_produto_cadastrar = tk.Label(janela_cadastrar_produtos, text="Código:", font=("Arial", 10, "bold"))
    label_codigo_produto_cadastrar.place(x=52, y=10)

    entry_codigo_produto_cadastrar = tk.Entry(janela_cadastrar_produtos, width=7, font=("Arial", 10))
    entry_codigo_produto_cadastrar.place(x=110, y=10)

    label_descricao_cadastrar = tk.Label(janela_cadastrar_produtos, text="Descrição:", font=("Arial", 10, "bold"))
    label_descricao_cadastrar.place(x=35, y=40)

    entry_descricao_cadastrar = tk.Entry(janela_cadastrar_produtos, width=50, font=("Arial", 10))
    entry_descricao_cadastrar.place(x=110, y=40)

    label_produto_ativo_cadastrar = tk.Label(janela_cadastrar_produtos, text="Produto Ativo:", font=("Arial", 10, "bold"))
    label_produto_ativo_cadastrar.place(x=655, y=40)

    produto_ativo = tk.BooleanVar()
    entry_produto_ativo_cadastrar = tk.Checkbutton(janela_cadastrar_produtos, variable=produto_ativo)
    entry_produto_ativo_cadastrar.place(x=750, y=40)

    label_unidade_medida_cadastrar = tk.Label(janela_cadastrar_produtos, text="Unidade:", font=("Arial", 10, "bold"))
    label_unidade_medida_cadastrar.place(x=45, y=100)

    entry_unidade_medida_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9, "bold"))
    entry_unidade_medida_cadastrar['values'] = UNIDADE_MEDIDA_PRODUTOS
    entry_unidade_medida_cadastrar.place(x=110, y=100)

    label_itens_embalagem_produtos_cadastrar = tk.Label(janela_cadastrar_produtos, text="Itens Embalagem:", font=("Arial", 10, "bold"))
    label_itens_embalagem_produtos_cadastrar.place(x=500, y=100)

    entry_itens_embalagem_produtos_cadastrar = tk.Entry(janela_cadastrar_produtos, font=("Arial", 10, "bold"))
    entry_itens_embalagem_produtos_cadastrar.place(x=625, y=100)

    label_subdescricao_cadastrar = tk.Label(janela_cadastrar_produtos, text="Subdescrição:", font=("Arial", 10, "bold"))
    label_subdescricao_cadastrar.place(x=10, y=150)

    entry_subdescricao_cadastar = tk.Entry(janela_cadastrar_produtos, width=50, font=("Arial", 10, "bold"))
    entry_subdescricao_cadastar.place(x=110, y=150)

    label_codigo_barras_cadastrar = tk.Label(janela_cadastrar_produtos, text="Código Barras:", font=("Arial", 10, "bold"))
    label_codigo_barras_cadastrar.place(x=520, y=150)

    entry_codigo_barras_cadastrar = tk.Entry(janela_cadastrar_produtos, font=("Arial", 10, "bold"))
    entry_codigo_barras_cadastrar.place(x=625, y=150)

    label_itens_pallete_cadastrar = tk.Label(janela_cadastrar_produtos, text="Itens Pallete:", font=("Arial", 10, "bold"))
    label_itens_pallete_cadastrar.place(x=530, y=200)

    entry_itens_pallete_cadastrar = tk.Entry(janela_cadastrar_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_pallete_cadastrar.place(x=625, y=200)

    label_itens_lastro_cadastrar = tk.Label(janela_cadastrar_produtos, width=9, text="Itens Lastro:", font=("Arial", 10, "bold"))
    label_itens_lastro_cadastrar.place(x=537, y=230)

    entry_itens_lastro_cadastrar = tk.Entry(janela_cadastrar_produtos, width=9, font=("Arial", 10, "bold"))
    entry_itens_lastro_cadastrar.place(x=625, y=230)

    label_grupo_produtos_cadastrar = tk.Label(janela_cadastrar_produtos, text="Grupo:", font=("Arial", 10, "bold"))
    label_grupo_produtos_cadastrar.place(x=55, y=200)

    entry_grupo_produtos_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9))
    entry_grupo_produtos_cadastrar["values"] = GRUPO_PRODUTOS
    entry_grupo_produtos_cadastrar.place(x=110, y=200)

    label_categorias_produtos_cadastrar = tk.Label(janela_cadastrar_produtos, text="Categoria:", font=("Arial", 10, "bold"))
    label_categorias_produtos_cadastrar.place(x=30, y=230)

    entry_categorias_produtos_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9))
    entry_categorias_produtos_cadastrar["values"] = CATEGORIAS_PRODUTOS
    entry_categorias_produtos_cadastrar.place(x=110, y=230)

    label_marca_produtos_cadastrar = ttk.Label(janela_cadastrar_produtos, text="Marca:", font=("Arial", 10, "bold"))
    label_marca_produtos_cadastrar.place(x=55, y=260)

    entry_marca_produtos_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9))
    entry_marca_produtos_cadastrar["values"] = MARCAS_PRODUTOS
    entry_marca_produtos_cadastrar.place(x=110, y=260)

    linha_horizontal_inferior = tk.Frame(janela_cadastrar_produtos, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=550)

    botao_confirmar_cadastrar = tk.Button(janela_cadastrar_produtos, text="Confirmar", font=("Arial", 10, "bold"), command=cadastrar_produto_gui)
    botao_confirmar_cadastrar.place(x=600, y=565)

    botao_cancelar_cadastrar = tk.Button(janela_cadastrar_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_cadastrar.place(x=700, y=565)

    lista_entrys = [
        entry_codigo_produto_cadastrar,
        entry_descricao_cadastrar,
        entry_unidade_medida_cadastrar,
        entry_itens_embalagem_produtos_cadastrar,
        entry_subdescricao_cadastar,
        entry_codigo_barras_cadastrar,
        entry_grupo_produtos_cadastrar,
        entry_categorias_produtos_cadastrar,
        entry_marca_produtos_cadastrar,
        entry_itens_pallete_cadastrar,
        entry_itens_lastro_cadastrar,
        botao_confirmar_cadastrar
    ]

    configurar_binds(lista_entrys, acoes_intermediarias=None, ultima_acao=cadastrar_produto_gui)