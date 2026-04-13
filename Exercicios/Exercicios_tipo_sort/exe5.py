lista = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
dicionario = {}

def agrupaPalavras(lis:list, dic:dict):
    for palavra in lis:
        letra = palavra[:1]
        if letra not in dic:
            dic[letra] = []
        dic[letra].append(palavra)

def organizaGrupos(dic:dict):
    for chave in dic:
        grupo = dic[chave]

        for i in range(len(grupo)):
            for j in range(len(grupo) - 1):
                if grupo[j].lower() > grupo[j+1].lower():
                    grupo[j], grupo[j+1] = grupo[j+1], grupo[j]

agrupaPalavras(lista, dicionario)
organizaGrupos(dicionario)

print(dicionario)

