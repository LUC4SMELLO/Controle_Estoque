from backend.models.produto import Produto

produto = Produto(2,
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
produto2 = Produto(2,
                  "Café",
                  "Pó de Café",
                  True,
                  "Unidade",
                  1,
                  123456789101213,
                  "Café",
                  "Pó",
                  "Menino da Porteira",
                  294,
                  45
                )

produto.entrada_estoque_produto(1000)



print(Produto.buscar_produto(2))