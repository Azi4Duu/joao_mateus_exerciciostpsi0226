palavras = ["Banana", "Uva", "abacaxi", "laranja", "papaya", "Guacamole", "Bananafe"]

def vemPrimeiro(palavra1, palavra2):
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()
    retorna = True
    """troca=""
    if len(palavra1)>len(palavra2):
        troca = palavra2
        palavra2 = palavra1
        palavra1 = troca"""
    for i in range(min(len(palavra1), len(palavra2))):
        if ord(palavra1[i]) < ord(palavra2[i]):
            retorna = True
            break
        elif ord(palavra1[i]) > ord(palavra2[i]):
            retorna = False
            break
    return retorna

for j in range(len(palavras)):
    for i in range(len(palavras)):
        trocaPalavra=""
        if i < len(palavras)-1:
            if not vemPrimeiro(palavras[i],palavras[i+1]):
                trocaPalavra = palavras[i+1]
                palavras[i+1] = palavras[i]
                palavras[i] = trocaPalavra

print(palavras)
    






