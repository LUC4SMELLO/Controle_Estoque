import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import inicializar_interface

def main():
    inicializar_interface()


if __name__ == "__main__":
    main()
