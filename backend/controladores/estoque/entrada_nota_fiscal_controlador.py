import os
import tkinter as tk
from datetime import datetime

from tkinter.filedialog import askopenfilename

from backend.controladores.produto.consultar_controlador import buscar_produto_back

from backend.controladores.estoque.entrada_controlador import entrada_produto_back

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

        ide_node = root.find(".//nfe:ide", namespaces=ns)
        if ide_node is not None:
            numero_nota = ide_node.find("nfe:nNF", namespaces=ns)
            if numero_nota is not None:
                numero_nota = numero_nota.text

        ender_emit_node = root.find(".//nfe:enderEmit", namespaces=ns)
        if ender_emit_node is not None:
            cidade_node = ender_emit_node.find("nfe:xMun", namespaces=ns)
            if cidade_node is not None:
                cidade = cidade_node.text
    
            uf_node = ender_emit_node.find("nfe:UF", namespaces=ns)
            if uf_node is not None:
                uf = uf_node.text

            bairro_node = ender_emit_node.find("nfe:xBairro", namespaces=ns)
            if bairro_node is not None:
                bairro = bairro_node.text

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
                codigo_produto = prod.find("nfe:cProd", namespaces=ns).text if prod.find("nfe:cProd", namespaces=ns) is not None else ""
                descricao = prod.find("nfe:xProd", namespaces=ns).text if prod.find("nfe:xProd", namespaces=ns) is not None else ""
                unidade = prod.find("nfe:uCom", namespaces=ns).text if prod.find("nfe:uCom", namespaces=ns) is not None else ""
                quantidade_text = prod.find("nfe:qCom", namespaces=ns).text if prod.find("nfe:qCom", namespaces=ns) is not None else "0"
                
                try:
                    quantidade = round(float(quantidade_text), 2)
                except ValueError:
                    quantidade = 0.0

                # Adiciona os dados do produto atual à lista
                todos_os_produtos.append({
                    "numero_nota": numero_nota,
                    "cidade": cidade,
                    "uf": uf,
                    "bairro": bairro,
                    "cnpj": cnpj,
                    "razao_social": razao_social,
                    "fantasia": fantasia,
                    "codigo_produto": codigo_produto,
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

def data_entrada_atual():

    data_agora = datetime.now()
    data_formatada = data_agora.strftime("%d/%m/%Y")

    return data_formatada

def verificar_produtos_da_nota_fiscal(nota_fiscal):

    produtos_nao_encontrados = ""

    for produto_dict in nota_fiscal:

        valido, _ = buscar_produto_back(produto_dict["codigo_produto"])
        if not valido:
            produtos_nao_encontrados = produtos_nao_encontrados + f"{produto_dict["codigo_produto"]} - {produto_dict["descricao"]}\n"
        
    if produtos_nao_encontrados:
        return False, produtos_nao_encontrados
    
    return True, "Todos os Produtos Foram Encontrados."

def entrada_produto_nota_fiscal_back(nota_fiscal):

    for produto_dict in nota_fiscal:
        entrada_produto_back(produto_dict["codigo_produto"], produto_dict["quantidade"])
    

