import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

import xml.etree.ElementTree as ET

def buscar_nota_fiscal_back():
    # Esconde a janela principal do Tkinter, já que a usaremos apenas para o filedialog
    root = tk.Tk()
    root.withdraw() 

    arquivo_escolhido = askopenfilename(
        title="Selecione o arquivo XML da Nota Fiscal",
        filetypes=[("Arquivos XML", "*.xml"), ("Todos os arquivos", "*.*")]
    )

    # Se nenhum arquivo for escolhido, a função retorna uma string vazia
    if not arquivo_escolhido:
        print("Nenhum arquivo XML selecionado.")
        return [] # Retorna uma lista vazia se nenhum arquivo for selecionado

    # NAMESPACE
    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

    # Lista para armazenar os dados de todos os produtos
    todos_os_produtos = []
    
    # Não precisa de loop "for arquivo in arquivo_escolhido", pois askopenfilename retorna apenas um arquivo
    try:
        tree = ET.parse(arquivo_escolhido)
        root = tree.getroot()

        # Extrair informações do emitente uma vez por arquivo
        cnpj = ""
        razao_social = ""
        fantasia = ""

        emit_node = root.find(".//nfe:emit", namespaces=ns)
        if emit_node is not None:
            cnpj_node = emit_node.find("nfe:CNPJ", namespaces=ns)
            if cnpj_node is not None:
                cnpj = cnpj_node.text

            razao_social_node = emit_node.find("nfe:xNome", namespaces=ns) # Corrigido para xNome
            if razao_social_node is not None:
                razao_social = razao_social_node.text

            fantasia_node = emit_node.find("nfe:xFant", namespaces=ns)
            if fantasia_node is not None:
                fantasia = fantasia_node.text

        for det in root.findall(".//nfe:det", namespaces=ns):
            prod = det.find("nfe:prod", namespaces=ns)

            if prod is not None:
                codigo = prod.find("nfe:cProd", namespaces=ns).text if prod.find("nfe:cProd", namespaces=ns) is not None else ""
                descricao = prod.find("nfe:xProd", namespaces=ns).text if prod.find("nfe:xProd", namespaces=ns) is not None else ""
                unidade = prod.find("nfe:uCom", namespaces=ns).text if prod.find("nfe:uCom", namespaces=ns) is not None else ""
                quantidade_text = prod.find("nfe:qCom", namespaces=ns).text if prod.find("nfe:qCom", namespaces=ns) is not None else "0"
                
                try:
                    quantidade = round(float(quantidade_text), 2)
                except ValueError:
                    quantidade = 0.0

                # Adiciona os dados do produto atual à lista
                todos_os_produtos.append({
                    "cnpj": cnpj,
                    "razao_social": razao_social,
                    "fantasia": fantasia,
                    "codigo": codigo,
                    "descricao": descricao,
                    "unidade": unidade,
                    "quantidade": quantidade
                })
        
        return todos_os_produtos # Retorna a lista completa de produtos
        
    except ET.ParseError as e:
        print(f"Erro ao analisar o arquivo XML: {e}")
        return []
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_escolhido}")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return []
