import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controladores.apartado.apartar import apartar_back
from backend.validadores.apartado.apartar import validar_apartado

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds


def criar_janela_apartar():

    def apartar_gui():

        data = entry_data.get().strip()
        codigo_produto = entry_codigo_produto.get().strip()
        quantidade = entry_quantidade.get().strip()
        motivo = entry_motivo_entrada.get().strip()

        valido, mensagem = validar_apartado(data, codigo_produto, quantidade, motivo)
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_data.focus_set()
            return None
        
        apartar_back(data, codigo_produto, quantidade, motivo)

        messagebox.showinfo("Sucesso!", "Produto Apartado.")
        entry_data.focus_set()

        entry_data.delete(0, tk.END)
        entry_codigo_produto.delete(0, tk.END) 
        entry_quantidade.delete(0, tk.END) 
        entry_motivo_entrada.delete(0, tk.END) 


    janela_apartar = tk.Toplevel()
    janela_apartar.title("Apartar")
    janela_apartar.geometry("500x230")
    janela_apartar.resizable(False, False)

    label_data = tk.Label(janela_apartar, text="Data:", font=LABEL)
    label_data.place(x=80, y=10)

    entry_data = tk.Entry(janela_apartar, width=10, font=ENTRY)
    entry_data.place(x=120, y=10)

    label_codigo_produto = tk.Label(janela_apartar, text="Código Produto:", font=LABEL)
    label_codigo_produto.place(x=10, y=50)

    entry_codigo_produto = tk.Entry(janela_apartar, width=10, font=ENTRY)
    entry_codigo_produto.place(x=120, y=50)

    label_quantidade = tk.Label(janela_apartar, text="Quantidade:", font=LABEL)
    label_quantidade.place(x=35, y=90)

    entry_quantidade = tk.Entry(janela_apartar, width=10, font=ENTRY)
    entry_quantidade.place(x=120, y=90)

    label_motivo_entrada = tk.Label(janela_apartar, text="Motivo:", font=LABEL)
    label_motivo_entrada.place(x=66, y=150)

    entry_motivo_entrada = tk.Entry(janela_apartar, width=49,font=ENTRY)
    entry_motivo_entrada.place(x=120, y=150)
    


    linha_horizontal_inferior = tk.Frame(janela_apartar, background="silver", height=5, width=800)
    linha_horizontal_inferior.place(x=0, y=180)

    botao_confirmar_apartar = tk.Button(janela_apartar, text="Confirmar", font=BOTAO, command=apartar_gui)
    botao_confirmar_apartar.place(x=300, y=195)

    botao_cancelar_apartar = tk.Button(janela_apartar, text="Cancelar", font=BOTAO)
    botao_cancelar_apartar.place(x=400, y=195)

    lista_entrys = [
            entry_data,
            entry_codigo_produto,
            entry_quantidade,
            entry_motivo_entrada,
            botao_confirmar_apartar
            ]
    
    acoes_intermediarias = [None, None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, apartar_gui)
