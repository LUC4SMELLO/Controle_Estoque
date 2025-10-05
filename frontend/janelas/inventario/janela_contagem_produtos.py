import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds


def criar_janela_contagem_produtos():

    janela_contagem_produtos = tk.Toplevel()
    janela_contagem_produtos.title("Contagem Produtos")
    janela_contagem_produtos.geometry("1920x1080")

    janela_contagem_produtos.state("zoomed")

    # LEITURA DO CSV
    arquivo_csv = "arquivos/PRODUTOS.CSV"  # arquivo recebido da API

    df = pd.read_csv(arquivo_csv,
                     header=0,
                     delimiter=";",
                     encoding="ISO-8859-1",
                     index_col=False
                    )
    
    df["Saldo Atual"] = df["Saldo Atual"].str.strip()


    # FRAME ROLÁVEL
    frame_container = tk.Frame(janela_contagem_produtos)
    frame_container.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_container)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # FRAME INTERNO
    frame_tabela = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_tabela, anchor="nw")

    # CABEÇALHOS
    tk.Label(frame_tabela, text="Código", font=("Arial", 15, "bold"), width=15, borderwidth=2, relief="ridge").grid(row=0, column=0)
    tk.Label(frame_tabela, text="Descrição", font=("Arial", 15, "bold"), width=40, borderwidth=2, relief="ridge").grid(row=0, column=1)
    tk.Label(frame_tabela, text="Quantidade", font=("Arial", 15, "bold"), width=15, borderwidth=2, relief="ridge").grid(row=0, column=2)

    # LISTA PARA ARMAZENAR AS ENTRADAS DE QUANTIDADES
    entradas_quantidade = []

    # EXIBE DADOS
    for i, linha in df.iterrows():
        tk.Label(frame_tabela, text=linha["Codigo"], width=15, borderwidth=1, relief="solid").grid(row=i+1, column=0)
        tk.Label(frame_tabela, text=linha["DescriÃ§Ã£o"], width=40, borderwidth=1, relief="solid", anchor="w").grid(row=i+1, column=1)
        
        entrada = tk.Entry(frame_tabela, width=15)
        if not linha["Saldo Atual"]:
            entrada.insert(0, 0)
        entrada.insert(0, linha["Saldo Atual"])
        entrada.grid(row=i+1, column=2)
        entradas_quantidade.append(entrada)

    # FUNÇÃO SALVAR
    def salvar():
        for i, entrada in enumerate(entradas_quantidade):
            novo_valor = entrada.get()
            try:
                df.at[i, "quantidade"] = int(novo_valor)
            except ValueError:
                messagebox.showerror("Erro", f"Valor inválido na linha {i+1}")
                janela_contagem_produtos.focus_set()
                return None
            
        df.to_csv(arquivo_csv, sep=";", index=False)
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")

    # BOTÃO SALVAR
    botao_salvar = tk.Button(janela_contagem_produtos, text="Salvar alterações", command=salvar, bg="green", fg="white", font=("Arial", 12, "bold"))
    botao_salvar.pack(pady=10)

    # HABILA ROLAGEM COM O MOUSE
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
