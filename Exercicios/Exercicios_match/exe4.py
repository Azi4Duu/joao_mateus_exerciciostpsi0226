<<<<<<< HEAD
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
=======
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
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
        print("Tipo desconhecido")