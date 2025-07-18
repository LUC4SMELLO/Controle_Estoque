from datetime import datetime

def validar_formulario_entrada_saida_estoque(
        data_entrada,
        codigo_produto,
        quantidade,
        motivo
):
    if not data_entrada or not codigo_produto or not quantidade or not motivo:
        return False, "Todos os Campos Devem ser Preechidos."
    
    try:
        datetime.strptime(data_entrada, "%d/%m/%Y")
    except ValueError:
        return False, "Digite uma Data Válida."
    
    if int(quantidade) <= 0:
        return False, "Digite uma Quantidade Válida."
    
    return True, "Entrada Válida."