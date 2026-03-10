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
        print("Estado desconhecido")