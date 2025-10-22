import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tkcalendar import DateEntry

from backend.constantes.date_entry import (
    BACKGROUND,
    FOREGROUND,
    HEADERSBACKGROUD,
    HEADERSFOREGROUD,
    NORMALBACKGROUND,
    NORMALFOREGROUND,
    WEEKENDBACKGROUND,
    WEEKENDFOREGROUND,
    SELECTBACKGROUND,
    SELECTFOREGROUND,
    BORDERCOLOR,
    BORDERWIDTH
)


from backend.validadores.estoque.formulario_entrada_saida import validar_formulario_entrada_saida_estoque

from backend.controladores.estoque.saida_controlador import saida_produto_back

from backend.controladores.produto.consultar_controlador import buscar_produto_back

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds 

def criar_janela_saida_produtos():

    def saida_produto_gui():

        codigo_produto = entry_codigo_produto_saida
        quantidade = entry_quantidade_saida


        valido, mensagem = validar_formulario_entrada_saida_estoque(
            entry_data_saida.get().strip(),
            entry_codigo_produto_saida.get().strip(),
            entry_quantidade_saida.get().strip(),
            entry_motivo_saida.get("1.0", tk.END)
        )
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_data_saida.focus_set()
            return None
    
        valido, resposta = buscar_produto_back(codigo_produto.get().strip())
        if not valido:
            messagebox.showerror("Erro", resposta)
            codigo_produto.focus_set()
            return None
        

        saida_produto_back(codigo_produto, quantidade)

        messagebox.showinfo("Sucesso!", "Saída Concluída.")
        entry_data_saida.focus_set()

        entry_data_saida.delete(0, tk.END)
        entry_codigo_produto_saida.delete(0, tk.END)
        entry_quantidade_saida.delete(0, tk.END)
        entry_motivo_saida.delete("1.0", tk.END)

    def fechar_janela_saida_produto():

        janela_saida_produtos.destroy()

    janela_saida_produtos = tk.Toplevel()
    janela_saida_produtos.title("Saída Produto")
    janela_saida_produtos.geometry("400x300")


    label_data_saida = tk.Label(janela_saida_produtos, text="Data Saída:", font=LABEL)
    label_data_saida.place(x=38, y=10)

    entry_data_saida = DateEntry(
        janela_saida_produtos,
        justify = "center", 
        font = ENTRY,
        background        = BACKGROUND,          # Background color of the entry field
        foreground        = FOREGROUND,          # Text color in the entry field
        headersbackground = HEADERSBACKGROUD,    # Background color of the month/year headers in the calendar popup
        headersforeground = HEADERSFOREGROUD,    # Text color of the month/year headers
        normalbackground  = NORMALBACKGROUND,    # Background color of normal days in the calendar popup
        normalforeground  = NORMALFOREGROUND,    # Text color of normal days
        weekendbackground = WEEKENDBACKGROUND,   # Background color of weekend days
        weekendforeground = WEEKENDFOREGROUND,   # Text color of weekend days
        selectbackground  = SELECTBACKGROUND,    # Background color of the selected day
        selectforeground  = SELECTFOREGROUND,    # Text color of the selected day
        bordercolor       = BORDERCOLOR,         # Border color of the calendar popup
        borderwidth       = BORDERWIDTH,
        selectmode = 'day',
        date_pattern = 'dd/mm/yyyy')
    
    entry_data_saida.place(x=120, y=10)

    label_codigo_produto = tk.Label(janela_saida_produtos, text="Código Produto:", font=LABEL)
    label_codigo_produto.place(x=10, y=50)

    entry_codigo_produto_saida = tk.Entry(janela_saida_produtos, width=10, font=ENTRY)
    entry_codigo_produto_saida.place(x=120, y=50)

    label_quantidade_saida = tk.Label(janela_saida_produtos, text="Quantidade:", font=LABEL)
    label_quantidade_saida.place(x=34, y=90)

    entry_quantidade_saida = tk.Entry(janela_saida_produtos, width=10, font=ENTRY)
    entry_quantidade_saida.place(x=120, y=90)

    label_motivo_saida = tk.Label(janela_saida_produtos, text="Motivo:", font=LABEL)
    label_motivo_saida.place(x=66, y=150)

    entry_motivo_saida = tk.Text(janela_saida_produtos, width=35, height=3, font=ENTRY)
    entry_motivo_saida.place(x=120, y=150)

    linha_horizontal_inferior = tk.Frame(janela_saida_produtos,  background="silver", width=500, height=5)
    linha_horizontal_inferior.place(x=0, y=250)

    botao_confirmar_saida = tk.Button(janela_saida_produtos, text="Confirmar", font=BOTAO, command=saida_produto_gui)
    botao_confirmar_saida.place(x=200, y=265)

    botao_cancelar_saida = tk.Button(janela_saida_produtos, text="Cancelar", font=BOTAO, command=fechar_janela_saida_produto)
    botao_cancelar_saida.place(x=300, y=265)


    lista_entrys = [entry_data_saida,
                    entry_codigo_produto_saida,
                    entry_quantidade_saida,
                    entry_motivo_saida,
                    botao_confirmar_saida
                    ]
    
    acoes_intermediarias = [None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, saida_produto_gui)