import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.constantes.fontes import LABEL, ENTRY, BOTAO

from backend.binds.configuracao_binds import configurar_binds

from backend.controladores.apartado.historico_apartado import buscar_historico_apartados_back

from backend.validadores.apartado.validar_historico_apartados import validar_historico


def criar_janela_historico_apartados():

    def buscar_apartados_gui():

        data = entry_data.get().strip()
        codigo_produto = entry_codigo_produto.get().strip()
        motivo = entry_motivo.get().strip()

        valido, mensagem = validar_historico(data, codigo_produto)
        if not valido:
            messagebox.showerror("Erro", mensagem)
            entry_data.focus_set()
            return False

        resultado = buscar_historico_apartados_back(data, codigo_produto, motivo)

        for item in treeview_apartados.get_children():
            treeview_apartados.delete(item)

        for linha in resultado:
            treeview_apartados.insert("", "end", values=linha)

        if not resultado:
            messagebox.showinfo("Aviso", "Não Há Apartados a Serem Listado.")
            entry_data.focus_set()

            entry_data.delete(0, tk.END)
            entry_codigo_produto.delete(0, tk.END)
            entry_motivo.delete(0, tk.END)

            return None


    janela_historico_apartar = tk.Toplevel()
    janela_historico_apartar.title("Histórico Apartados")
    janela_historico_apartar.geometry("1100x600")
    janela_historico_apartar.resizable(False, False)


    label_data = tk.Label(janela_historico_apartar, text="Data:", font=LABEL)
    label_data.place(x=20, y=20)

    entry_data = tk.Entry(janela_historico_apartar, width=10, font=ENTRY)
    entry_data.place(x=60, y=20)

    label_codigo_produto = tk.Label(janela_historico_apartar, text="Código Produto:", font=LABEL)
    label_codigo_produto.place(x=150, y=20)

    entry_codigo_produto = tk.Entry(janela_historico_apartar, width=10, font=ENTRY)
    entry_codigo_produto.place(x=260, y=20)

    label_motivo = tk.Label(janela_historico_apartar, text="Motivo:", font=LABEL)
    label_motivo.place(x=350, y=20)

    entry_motivo = tk.Entry(janela_historico_apartar, width=49, font=ENTRY)
    entry_motivo.place(x=405, y=20)


    botao_buscar_apartados = tk.Button(janela_historico_apartar, text="Buscar", font=BOTAO, command=buscar_apartados_gui)
    botao_buscar_apartados.place(x=800, y=17)


    linha_horizontal_superior = tk.Frame(janela_historico_apartar, background="silver", width=1100, height=5)
    linha_horizontal_superior.place(x=0, y=80)




    scrollbar_vertical = ttk.Scrollbar(janela_historico_apartar, orient="vertical")
    scrollbar_vertical.place(x=1062, y=110, height=270)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    colunas = ("data", "codigo_produto", "descricao", "quantidade", "motivo")
    treeview_apartados = ttk.Treeview(
        janela_historico_apartar,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical.set
    )
    treeview_apartados.place(x=20, y=110, width=1035, height=270)

    scrollbar_vertical.config(command=treeview_apartados.yview)

    treeview_apartados.heading("data", text="DATA", anchor="center")
    treeview_apartados.heading("codigo_produto", text="CÓDIGO PRODUTO", anchor="center")
    treeview_apartados.heading("descricao", text="DESCRIÇÃO", anchor="center")
    treeview_apartados.heading("quantidade", text="QUANTIDADE", anchor="center")
    treeview_apartados.heading("motivo", text="MOTIVO", anchor="center")

    treeview_apartados.column("data", width=120, anchor="center")
    treeview_apartados.column("codigo_produto", width=160, anchor="center")
    treeview_apartados.column("descricao", width=220, anchor="center")
    treeview_apartados.column("quantidade", width=120, anchor="center")
    treeview_apartados.column("motivo", width=120, anchor="center")
    # endregion

    linha_horizontal_inferior = tk.Frame(janela_historico_apartar, background="silver", width=1100, height=5)
    linha_horizontal_inferior.place(x=0, y=550)




    lista_entrys = [entry_data, entry_codigo_produto, entry_motivo, botao_buscar_apartados]
    
    acoes_intermediarias = [None, None, None, None]

    configurar_binds(lista_entrys, acoes_intermediarias, ultima_acao=buscar_apartados_gui)
