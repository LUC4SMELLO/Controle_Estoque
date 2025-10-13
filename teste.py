import tkinter as tk
from tkinter import ttk
import threading
import time
import queue

# -----------------------
# Exemplo 1: Barra indeterminada (marquee)
# -----------------------
def mostrar_loading_indeterminado():
    win = tk.Toplevel(root)
    win.title("Carregando...")
    win.geometry("400x100")
    win.resizable(False, False)

    label = ttk.Label(win, text="Processando, por favor aguarde...")
    label.pack(pady=(10, 6))

    pb = ttk.Progressbar(win, mode="indeterminate", length=350)
    pb.pack(padx=10, pady=(0, 10))

    # Começa animação indeterminada (valor em ms do "intervalo")
    pb.start(10)  # quanto menor, mais rápido o movimento

    # Simula tarefa demorada em thread (substitua por sua função)
    def tarefa():
        time.sleep(4)  # substitua por sua lógica
        # Ao terminar, pare a barra e feche a janela pela thread principal:
        win.after(0, lambda: (pb.stop(), win.destroy()))

    threading.Thread(target=tarefa, daemon=True).start()


# -----------------------
# Exemplo 2: Barra determinada (percentual) usando queue
# -----------------------
def mostrar_loading_determinado():
    win = tk.Toplevel(root)
    win.title("Processando (0%)")
    win.geometry("450x120")
    win.resizable(False, False)

    label = ttk.Label(win, text="Fazendo o processamento...")
    label.pack(pady=(8, 6))

    # Variável de texto para mostrar percentual
    pct_var = tk.StringVar(value="0%")
    pct_label = ttk.Label(win, textvariable=pct_var)
    pct_label.pack()

    pb = ttk.Progressbar(win, mode="determinate", length=400, maximum=100)
    pb.pack(padx=10, pady=(6, 10))

    q = queue.Queue()

    # Função que atualiza a GUI a partir da fila
    def checar_fila():
        try:
            while True:
                progresso = q.get_nowait()
                pb['value'] = progresso
                pct_var.set(f"{int(progresso)}%")
                win.title(f"Processando ({int(progresso)}%)")
                if progresso >= 100:
                    # pequena pausa para o usuário ver 100% e então fechar
                    win.after(300, win.destroy)
        except queue.Empty:
            # Nenhum item, continua checando
            win.after(100, checar_fila)

    # Exemplo de trabalho que reporta progresso (substitua pelo seu)
    def tarefa_com_progresso(q):
        total = 20
        for i in range(total + 1):
            time.sleep(0.18)  # trabalho fictício
            pct = (i / total) * 100
            q.put(pct)
        # garante 100 no final
        q.put(100)

    threading.Thread(target=tarefa_com_progresso, args=(q,), daemon=True).start()
    checar_fila()


# -----------------------
# Exemplo de uso na janela principal
# -----------------------
root = tk.Tk()
root.title("Exemplos de Loading")
root.geometry("320x180")

btn_ind = ttk.Button(root, text="Mostrar Loading Indeterminado", command=mostrar_loading_indeterminado)
btn_ind.pack(pady=(20, 8), padx=12, fill="x")

btn_det = ttk.Button(root, text="Mostrar Loading Determinado", command=mostrar_loading_determinado)
btn_det.pack(pady=(0, 8), padx=12, fill="x")

# Exemplo de função "real" que você pode usar para substituir a simulação:
# def minha_funcao_longa(progress_callback):
#     for i in range(100):
#         fazer_algo()
#         progress_callback(i+1)  # repassa valor (1..100)
#
# E para integrar, o thread chamaria minha_funcao_longa(lambda p: q.put(p))

root.mainloop()
