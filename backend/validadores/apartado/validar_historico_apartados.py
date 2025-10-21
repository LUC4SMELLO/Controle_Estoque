from datetime import datetime

from backend.controladores.produto.consultar_controlador import buscar_produto_back


def validar_historico(data, codigo_produto):

    if data:
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            return False, "Digite uma Data Válida."

    if codigo_produto:
        valido, mensagem = buscar_produto_back(codigo_produto)
        if not valido:
            return False, mensagem
        
    return True, "Histórico Válido."
