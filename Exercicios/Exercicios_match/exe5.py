<<<<<<< HEAD
mensagem=input("Escreva uma mensagem: ").lower()

match mensagem:
    case m if m == "olá" or m == "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
=======
mensagem=input("Escreva uma mensagem: ").lower()

match mensagem:
    case m if m == "olá" or m == "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
        print("Mensagem generica")