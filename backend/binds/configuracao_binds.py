def configurar_binds(entries: list, acoes_intermediarias=None, ultima_acao=None):
    """
    Configura as binds das entrys.

    Parameters
    ----------
        entries
            Uma lista com todas as entries.
        acoes_intermediarias
            Uma lista de ações intermediarias (caso existam).
        ultima_acao
            Última ação a ser executada.

    Returns
    ----------
        None
    """
    total = len(entries)
    acoes_intermediarias = acoes_intermediarias or [None] * total

    for i, entry in enumerate(entries):
        def acao(e, i=i):
            if acoes_intermediarias[i]:
                acoes_intermediarias[i]()
            if i < total - 1:
                entries[i + 1].focus_set()
            elif ultima_acao:
                ultima_acao()

        entry.bind("<Return>", acao)