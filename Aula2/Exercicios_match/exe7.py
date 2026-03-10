produto={"categoria" : input("categoria: ").lower(), "preco" : int(input("preço: "))}

match produto:
    case {"categoria" : "eletronico", "preco" : p} if p > 1000:
        print("Produto de luxo")
    case {"categoria" : "eletronico", "preco" : p} if p <= 1000:
        print("Produto comum")
    case {"categoria" : "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")