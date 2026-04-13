dicionario = {"a" : 1, "b" : 2, "c" : 3}
dicionario2 = {}

def troca(d:dict, d2:dict):
    for pos in d:
        d2.update({d[pos] : pos})

troca(dicionario, dicionario2)
print(dicionario2)