import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import inicializar_interface
from servicos.servico_banco_dados import inicializar_bancos_de_dados

def main():
    inicializar_bancos_de_dados()
    inicializar_interface()


if __name__ == "__main__":
    main()
