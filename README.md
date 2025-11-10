# Controle de Estoque

## Descrição

Este software foi desenvolvido para gerenciar o estoque de uma empresa, oferecendo uma série de funcionalidades que permitem o controle de produtos, entradas e saídas, fornecedores, pendências de entrega e apartados.

## Tecnologias

**Python 3.13.1** <br>
**Tkinter 8.6.** <br>
**SQLite3 3.13.1** <br>

## Funcionalidades

1. **Produtos** <br>
    Cadastrar <br> 
    Alterar <br>
    Excluir <br>
    Consultar <br>

2. **Estoque** <br>
    Entrada por Nota Fiscal <br>
    Entrada <br>
    Saída <br>

3. **Apartados** <br>
    Apartar <br>
    Histórico <br>

4. **Pendências** <br>
    Histórico <br>

5. **Inventário** <br>
    Digitação Produtos <br>
    Digitação Doces <br>
    Ajustar Diferenças <br>
    Comparar Estoque <br>

6. **Fornecedores** <br>
    Cadastrar <br>
    Alterar <br>
    Excluir <br>
    Consultar <br>

## Estrutura Banco de Dados

1. **`Produtos`** <br>
    *codigo_produto* - É o código do produto (SKU). <br>
    *descricao* - Armazena a descrição do produto. <br>
    *subdescricao* - Contém a subdescrição do produto. <br>
    *produto_ativo* - Produto está ativo ou não. <br>
    *unidade_medida* - A unidade de medida do produto. <br>
    *itens_embalagem* - Quantidade de itens por embalagem. <br>
    *codigo_barras* - O código de barras. <br>
    *grupo* - O grupo que o produto pertence. <br>
    *categoria* - A categoria do produto. <br>
    *marca* - A marca do produto. <br>
    *itens_pallete* - Quantidade de itens por pallete. <br>
    *itens_lastro* - Quantiadade de itens por lastro. <br>
    *quantidade_estoque* - Quantidade do produto no estoque. <br>

2. **`Apartado`** <br>
    *data* - A data da ocorrência. <br>
    *codigo_produto* - O código do produto. <br>
    *quantidade* - A quantidade que vai ser apartada. <br>
    *motivo* - O motivo do apartado. <br>

3. **`Pendência`** <br>
    *cupom* - O número da pendência.
    *data_ocorrencia* - A data do cadastro da pendência.
    *codigo_cliente* - O código do cliente.
    *razao_social* - A razão social do cliente.
    *cidade* - A cidade do cliente.
    *vendedor* - O vendedor que atende o cliente.
    *codigo_produto* - O código do produto.
    *quantidade* - A quantidade do produto.

4. **`Fornecedores`** <br>
    *codigo_fornecedor* - O código do fornecedor. <br>
    *razao_social* - A razão social do fornecedor. <br>
    *nome_fantasia* - O nome fantasia do fornecedor. <br>
    *fornecedor_ativo* - Se o fornecedor está ativo ou não. <br>
    *cnpj* - O CNPJ do fornecedor. <br>
    *inscricao_estadual* - A inscrição estadual do fornecedor. <br>
    *logradouro* - Endereço do fornecedor. <br>
    *bairro* - O nome do bairro. <br>
    *cidade* - O nome da cidade. <br>
    *cep* - O número do CEP. <br>
    *estado* - A sigla do estado. <br>

5. **`Notas Fiscais`** <br>
    *numero_nota_fiscal* - O número da nota fiscal.
    *codigo_fornecedor* - O código do fornecedor.
    *data_entrada* - A data da entrada.

6. **`Itens Notas Fiscais`** <br>
    *data_entrada* - A data da entrada. <br>
    *numero_nota_fiscal* - O número da nota fiscal. <br>
    *codigo_fornecedor* - O código do fornecedor. <br>
    *codigo_produto* - O código do produto. <br>
    *descricao* - A descrição do produto. <br>
    *quantidade* - A quantidade do produto. <br>
    *preco_unitario* - Preço unitário do produto. <br>
    *preco_total* - O preço total do produto. <br>




## Observações

- Interface gráfica desenvolvida com **Tkinter**
- Banco de dados local feito com **SQLite3**
- Projeto desenvolvido para pequenos e médios comércios