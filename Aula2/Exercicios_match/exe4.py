valor = eval(input("Introduz um valor: "))

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case list():
        print("Lista")
    case str():
        if valor.isnumeric():
            print("String numérica")
        else:
            print("String textual")
    case _:
        print("Tipo desconhecido")