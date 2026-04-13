palavra = input("Introduza uma palavra: ")
dicionario = {}

def partirPalavra(dic:dict, w:str):
    for l in w:
        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 1

partirPalavra(dicionario, palavra)
print(dicionario)