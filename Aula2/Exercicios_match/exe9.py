req={"metodo" : input("metodo: ").upper(), "conteudo" : input("conteudo: ")}

match req:
    case {"metodo" : "GET"}:
        print("Requisição recebida")
    case {"metodo" : "POST", "conteudo" : c} if len(c)>0:
        print("Requisição POST com dados válidos")
    case {"metodo" : "POST", "conteudo" : c} if len(c)==0:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")