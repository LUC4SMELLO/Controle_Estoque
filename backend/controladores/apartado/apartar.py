from backend.models.apartado import Apartado

def apartar_back(data, codigo_produto, quantidade, motivo):

    novo_apartado = Apartado(data, codigo_produto, quantidade, motivo)
    novo_apartado.inserir_apartado()

    