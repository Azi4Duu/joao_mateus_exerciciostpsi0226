palavra = input("Digite uma palavra: ")

def ordenaLetras(pal:str):
    orden = []
    for letra in pal:
        orden.append(letra)
    
    for j in range(len(orden)):
        for k in range(len(orden)):
            if k < len(orden) - 1:
                if ord(orden[k]) > ord(orden[k+1]):
                    orden[k], orden[k+1] = orden[k+1], orden[k]
    pal = ""
    for letra in orden:
        pal += letra
    
    return pal

print(palavra)
print(ordenaLetras(palavra))
