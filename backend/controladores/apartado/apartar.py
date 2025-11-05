from backend.models.apartado import Apartado

def apartar_back(data, codigo_produto, quantidade, motivo):
    """
    Aparta um produto.

    Parameters
    ----------
        data
            Data atual.
        codigo_produto
            Código do produto a ser apartado.
        quantidade
            Quantidade do produto a ser apartado.
        motivo
            O motivo do apartado.

    Returns
    -------
        None
    """

    novo_apartado = Apartado(data, codigo_produto, quantidade, motivo)
    novo_apartado.inserir_apartado()

    