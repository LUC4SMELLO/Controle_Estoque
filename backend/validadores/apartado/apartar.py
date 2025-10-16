from datetime import datetime

from backend.controladores.produto.consultar_controlador import buscar_produto_back

def validar_apartado(data, codigo_produto, quantidade, motivo):

    if not data or not codigo_produto or not quantidade or not motivo:
        return False, "Todos os Campos Devem Estar Preechidos."
    
    if int(quantidade) < 0:
        return False, "Quantidade Inválida."
    
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return False, "Digite uma Data Válida."
    
    valido, mensagem = buscar_produto_back(codigo_produto)
    if not valido:
        return False, "Produto Não Encontrado."
    
    return True, "Apartado Válido."