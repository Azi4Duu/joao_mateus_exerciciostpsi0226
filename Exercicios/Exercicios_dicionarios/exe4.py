utilizador = {"Nome" : "Carlos", "Idade" : "28"}

def verifica(dic:dict):
    for key in dic:
        if key == "Email":
            return True
    return False

if verifica(utilizador):
    print("Email encontrado")
else:
    print("Email não encontrado")