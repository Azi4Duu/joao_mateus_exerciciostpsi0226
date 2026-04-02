tipo=input("Indique se é uma 'compra' ou 'venda': ")
valor=input("Indique o valor: ")

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")