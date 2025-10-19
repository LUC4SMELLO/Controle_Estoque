from database.banco_dados_produtos import criar_tabela_produtos
from database.banco_dados_fornecedores import criar_tabela_fornecedores
from database.banco_dados_nota_fiscal import criar_tabela_nota_fiscal
from database.banco_dados_itens_nota import criar_tabela_itens_nota_fiscal
from database.banco_dados_apartados import criar_banco_dados_apartados

def inicializar_bancos_de_dados():

    criar_tabela_produtos()
    criar_tabela_fornecedores()
    criar_tabela_nota_fiscal()
    criar_tabela_itens_nota_fiscal()
    criar_banco_dados_apartados()
