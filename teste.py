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

todos_produtos = Produto.listar_todos_produtos()

print(todos_produtos)
