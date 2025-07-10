def configurar_binds(entries: list, acoes_intermediarias=None, ultimas_acoes=None):
    """
    Aplica binds para navegar com Enter, e executar ações intermediárias.

    :param entries: lista de Entry widgets
    :param acoes_intermediarias: lista de funções a executar antes de passar para o próximo Entry
    :param on_last_enter: função a chamar ao pressionar Enter no último Entry
    """
    total = len(entries)
    acoes_intermediarias = acoes_intermediarias or [None] * total

    for i, entry in enumerate(entries):
        def acao(e, i=i):
            if acoes_intermediarias[i]:
                acoes_intermediarias[i]()
            if i < total - 1:
                entries[i + 1].focus_set()
            elif ultimas_acoes:
                ultimas_acoes()

        entry.bind("<Return>", acao)