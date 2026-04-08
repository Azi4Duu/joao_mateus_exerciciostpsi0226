dicionario1 = {"a" : 1, "b" : 2}
dicionario2 = {"c" : 3, "d" : 4}
juntos = {}

def juntar(d:dict, j:dict):
    for pos in d:
        j.update({pos : d[pos]})

juntar(dicionario1, juntos)
juntar(dicionario2, juntos)

print(juntos)