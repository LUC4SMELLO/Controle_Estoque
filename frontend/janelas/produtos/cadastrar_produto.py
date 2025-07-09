import tkinter as tk
from tkinter import ttk

def criar_janela_cadastrar_produto():

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
    entry_unidade_medida_cadastrar['values'] = (
        "CX 01 - CAIXA 01/01 UND",
        "CX 02 - CAIXA 02/01 UND",
        "CX 04 - CAIXA 04/01 UND",
        "CX 06 - CAIXA 06/01 UND",
        "CX 08 - CAIXA 08/01 UND",
        "CX 09 - CAIXA 09/01 UND",
        "CX 10 - CAIXA 10/01 UND",
        "CX 12 - CAIXA 12/01 UND",
        "CX 14 - CAIXA 14/01 UND",
        "CX 16 - CAIXA 16/01 UND",
        "CX 18 - CAIXA 18/01 UND",
        "CX 20 - CAIXA 20/01 UND",
        "CX 22 - CAIXA 22/01 UND",
        "CX 24 - CAIXA 24/01 UND",
        "CX 40 - CAIXA 40/01 UND",
        "CX 50 - CAIXA 50/01 UND",
        "CX 60 - CAIXA 60/01 UND",
        "CX 70 - CAIXA 70/01 UND", 
        "CX 80 - CAIXA 80/01 UND",
        "CX 90 - CAIXA 90/01 UND",
        "CX 100 - CAIXA 100/01 UND",
        "KG 01 - KG",
        "UND 01 - UNIDADE 01"
    )
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
    entry_grupo_produtos_cadastrar["values"] = (
        "001 - REFRIG",
        "002 - CERVEJA",
        "003 - AGUA",
        "004 - CHAS",
        "005 - ENERGÉTICO",
        "006 - HIDROTONICO",
        "007 - ISOTONICO",
        "008 - SUCOS",
        "009 - SOJA",
        "010 - ÁGUA DE COCO",
        "011 - LACTEO",
        "012 - SPIRITS",
        "013 - BALAS E ALIMENTOS",
        "014 - MIXED DRINKS",
        "019 - SNACKS",
        "020 - ALIMENTOS",
        "023 - GAS CO2",
        "099 - MATERIAL"
    )
    entry_grupo_produtos_cadastrar.place(x=110, y=200)

    label_categorias_produtos_cadastrar = tk.Label(janela_cadastrar_produtos, text="Categoria:", font=("Arial", 10, "bold"))
    label_categorias_produtos_cadastrar.place(x=30, y=230)

    entry_categorias_produtos_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9))
    entry_categorias_produtos_cadastrar["values"] = (
        "037 - 200 ML",
        "077 - 220 ML",
        "142 - 250 ML",
        "082 - 290 ML",
        "006 - 310 ML",
        "004 - 350 ML",
        "005 - 450 ML",
        "143 - 510 ML",
        "022 - 600 ML",
        "027 - 1 LITRO",
        "033 - 1.5 LITROS",
        "041 - 2 LITROS",
        "046 - 2.25 LITROS",
        "050 - 2.5 LITROS",
        "007 - 3 LITROS",
        "130 - 5 LITROS",
        "140 - 10 LITROS",
        "141 - 18 LITROS",
    )
    entry_categorias_produtos_cadastrar.place(x=110, y=230)

    label_marca_produtos_cadastrar = ttk.Label(janela_cadastrar_produtos, text="Marca:", font=("Arial", 10, "bold"))
    label_marca_produtos_cadastrar.place(x=55, y=260)

    entry_marca_produtos_cadastrar = ttk.Combobox(janela_cadastrar_produtos, width=25, font=("Arial", 9))
    entry_marca_produtos_cadastrar["values"] = (
        "001 - 3 MEDALLAS ",
        "001 - FINI",
        "001 - HALLS",
        "001 - JACK DANIEL'S",
        "001 - MATERIAL",
        "001 - MATTE COPO ",
        "001 - MATTE LEAO ",
        "001 - MENTOS",
        "001 - SMIRNOFF",
        "001 - WHITE MARTINS",
        "002 - 120 VINHOS",
        "002 - FRUITTELLA",
        "002 - ICE TEA",
        "002 - JOHNNIE WALKER",
        "002 - SCHWEPPES",
        "002 - SKYY",
        "002 - TRIDENT",
        "003 - TANQUERAY",
        "008 - BAVARIA",
        "010 - FANTA BAG",
        "011 - MATTE LEAO",
        "018 - BURN",
        "042 - COCA-COLA ",
        "048 - COCA-COLA ZERO ",
        "049 - COCA COLA ",
        "053 - SPRITE FRESH",
        "061 - DEL VALLE",
        "068 - FANTA",
        "071 - FANTA ZERO",
        "088 - KAISER ",
        "120 - DREHER" ,
        "122 - CYNAR",
        "123 - CAMPARI",
        "130 - CRYSTAL ",
        "140 - POWERADE ",
        "142 - CC ",
        "143 - ESTRELLA GALICIA ",
        "145 - THEREZÓPOLIS",
        "153 - SCHWEPPES",
        "174 - SPRITE",
        "176 - COCA",
        "200 - PETTIZ",
        "201 - PRINGLES",
        "202 - CHEEZ IT",
        "203 - OREO",
        "204 - KELLOG'S",
        "226 - CRYSTAL",
        "231 - DEL VALLE FRUT",
        "234 - DELL VALE MAIS",
        "237 - GUARAPAN ",
        "238 - KUAT",
        "241 - EISENBAHN",
        "242 - THEREZOPOLIS",
        "252 - KAPO",
        "265 - CHA ICE TEA",
        "279 - DEL VALLE FRUT",
        "279 - SOL PREMIUM ",
        "282 - Monster",
        "301 - ADES FRUTAS ",
        "302 - ADES ORIGINAL",
        "303 - ADES MAX",
        "450 - SAGATIBA",
        "451 - YPIÓCA",
        "999 - SPRITE"
    )
    entry_marca_produtos_cadastrar.place(x=110, y=260)




    linha_horizontal_inferior = tk.Frame(janela_cadastrar_produtos, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=550)

    bota_confirmar_cadastrar = tk.Button(janela_cadastrar_produtos, text="Confirmar", font=("Arial", 10, "bold"))
    bota_confirmar_cadastrar.place(x=600, y=565)

    botao_cancelar_cadastrar = tk.Button(janela_cadastrar_produtos, text="Cancelar", font=("Arial", 10, "bold"))
    botao_cancelar_cadastrar.place(x=700, y=565)