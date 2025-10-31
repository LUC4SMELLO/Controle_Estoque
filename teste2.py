from datetime import date

from backend.controladores.apartado.historico_apartado import buscar_historico_apartados_back

data = ""
codigo_produto = ""
motivo = ""

resultado = buscar_historico_apartados_back(data, codigo_produto, motivo)


data_atual = date.today()
data_atual_formatada = data_atual.strftime("%d/%m/%Y")

for i in resultado:
    if i[0] == data_atual_formatada:
        print("Data Atual!")