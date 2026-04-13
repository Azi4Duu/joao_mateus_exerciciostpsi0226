frase = input("Digite uma frase: ")
dicionario = {}

def contaPalavras(f:str, d:dict):
    for palavra in f.split(" ") :
        if palavra in d : 
            d[palavra] += 1
        else:
            d[palavra] = 1

contaPalavras(frase, dicionario)
print(dicionario)