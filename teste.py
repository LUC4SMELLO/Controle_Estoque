from backend.models.produto import Produto

produto = Produto(1,
                  "Refrigerante",
                  "Lata",
                  True,
                  "Unidade",
                  1,
                  123456789101213,
                  "Refrigerante",
                  "Bebida",
                  "Coca Cola",
                  294,
                  45
                )


print(produto.descricao)
