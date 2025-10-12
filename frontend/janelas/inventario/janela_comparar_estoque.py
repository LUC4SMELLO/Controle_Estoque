import tkinter as tk
from tkinter import messagebox, ttk

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

from backend.scripts.processar_diferencas_estoque import comparacao


def criar_janela_comparar_estoque():

    janela_comparar_estoque = tk.Toplevel()
    janela_comparar_estoque.title("Comparar Estoque")
    janela_comparar_estoque.geometry("1200x600")

    # FRAME ROLÁVEL
    frame_container = tk.Frame(janela_comparar_estoque)
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

    tk.Label(frame_tabela, text="Código", font=("Arial", 15, "bold"), width=10, height=2, borderwidth=2, relief="ridge").grid(row=0, column=0)
    tk.Label(frame_tabela, text="Descrição", font=("Arial", 15, "bold"), width=25, height=2, borderwidth=2, relief="ridge").grid(row=0, column=1)
    tk.Label(frame_tabela, text="Estoque\nContado", font=("Arial", 15, "bold"), width=10, borderwidth=2, relief="ridge").grid(row=0, column=2)
    tk.Label(frame_tabela, text="Apartado", font=("Arial", 15, "bold"), width=10, height=2, borderwidth=2, relief="ridge").grid(row=0, column=3)
    tk.Label(frame_tabela, text="Diferença", font=("Arial", 15, "bold"), width=10, height=2, borderwidth=2, relief="ridge").grid(row=0, column=4)
    tk.Label(frame_tabela, text="Estoque\nSistema", font=("Arial", 15, "bold"), width=10, height=2, borderwidth=2, relief="ridge").grid(row=0, column=5)
    tk.Label(frame_tabela, text="Status", font=("Arial", 15, "bold"), width=17, height=2, borderwidth=2, relief="ridge").grid(row=0, column=6)

    # EXIBE DADOS
    for i, linha in comparacao.iterrows():
        tk.Label(frame_tabela, text=linha["codigo_produto"], font=("Arial", 12), justify="center", width=5).grid(row=i+1, column=0)
        tk.Label(frame_tabela, text=linha["descricao"], font=("Arial", 12), justify="center", anchor="w", width=25).grid(row=i+1, column=1)
        tk.Label(frame_tabela, text=linha["quantidade_contada"], font=("Arial", 12), justify="center", anchor="center", width=5).grid(row=i+1, column=2)
        tk.Label(frame_tabela, text=linha["diferenca"], font=("Arial", 12), justify="center", width=10).grid(row=i+1, column=4)
        tk.Label(frame_tabela, text=linha["quantidade_sistema"], font=("Arial", 12), justify="center", width=10).grid(row=i+1, column=5)
        tk.Label(frame_tabela, text=linha["status"], font=("Arial", 12), justify="center", width=17).grid(row=i+1, column=6)

    # HABILA ROLAGEM COM O MOUSE
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-event.delta * 1 / 120), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    