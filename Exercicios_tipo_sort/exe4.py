lista = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contaOrdena(lis:list):
    orden = []
    for palavra in lista:
        count = 0
        for letra in palavra:
            if letra.islower():
                count += 1
        orden.append(count)

    for i in range(len(lis)):
        for j in range(len(lis)-1):
            if orden[j] > orden[j+1]:
                orden[j], orden[j+1] = orden[j+1], orden[j]
                lis[j], lis[j+1] = lis[j+1], lis[j]

contaOrdena(lista)
print(lista)