<<<<<<< HEAD
stat=input("status (ok/erro): ")
tdr=int(input("tempo_resposta: "))

match stat:
    case s if s == "ok":
        if tdr > 200:
            print("Servidor lento")
        else:
            print("Servidor ativo")
    case s if s == "erro":
        print("Servidor indisponível")
    case _:
=======
stat=input("status (ok/erro): ")
tdr=int(input("tempo_resposta: "))

match stat:
    case s if s == "ok":
        if tdr > 200:
            print("Servidor lento")
        else:
            print("Servidor ativo")
    case s if s == "erro":
        print("Servidor indisponível")
    case _:
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
        print("Estado desconhecido")