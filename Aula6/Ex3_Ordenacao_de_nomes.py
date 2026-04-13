nomes = ["Pedro Pereira", "Ana Beatriz", "Ana Clara", "Carlos Silva", "Beatriz Souza", "Ana Paula", "Pedro Andrade"]

palavra = "palavra ganda"

def ordenaNomes(lista:list):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            n1 = lista[j].split(sep=" ")
            n2 = lista[j+1].split(sep=" ")
            for k in range(min(len(n1[0]),len(n2[0]))):
                if ord(n1[0][k]) > ord(n2[0][k]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    break
                elif ord(n1[0][k]) < ord(n2[0][k]):
                    break
            else:
                for k in range(min(len(n1[1]),len(n2[1]))):
                    if ord(n1[1][k]) > ord(n2[1][k]):
                        lista[j], lista[j+1] = lista[j+1], lista[j]
                        break
                    elif ord(n1[1][k]) < ord(n2[1][k]):
                        break

ordenaNomes(nomes)
print(nomes)