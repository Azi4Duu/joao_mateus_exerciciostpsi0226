<<<<<<< HEAD
tipo=input("Indique se é uma 'compra' ou 'venda': ")
valor=input("Indique o valor: ")

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
=======
tipo=input("Indique se é uma 'compra' ou 'venda': ")
valor=input("Indique o valor: ")

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
        print("Pedido desconhecido")