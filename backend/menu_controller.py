# menu_controller.py
import frontend.menu_state as state

def organizar_botoes(menu_ativo):
    y = 10
    for nome, botao in state.botoes_principais.items():
        botao.place(x=10, y=y)
        y += 50

        for sub in state.botoes_submenus.get(nome, []):
            sub.place_forget()

        if nome == menu_ativo:
            for sub in state.botoes_submenus[nome]:
                sub.place(x=30, y=y)
                y += 30

    state.submenu_ativo = menu_ativo
