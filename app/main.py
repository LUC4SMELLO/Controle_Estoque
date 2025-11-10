import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import inicializar_interface
from servicos.servico_banco_dados import inicializar_bancos_de_dados
from backend.scripts.processar_pendencias_estoque import processar_pendencias

def main():
    inicializar_bancos_de_dados()
    processar_pendencias()
    inicializar_interface()


if __name__ == "__main__":
    main()
