notas = {"João" : [7, 8, 9], "Maria" : [10, 9, 8], "Ana" : [6, 7, 8]}

def calculaMedia(d: dict):
    for nome in d:
        """soma = 0
        for n in d[nome]:
            soma += n 
            media = soma / len(d[nome])
        print(f"{nome}: {media}")"""
        print(f"{nome}: {sum(d[nome])/len(d[nome])}")

calculaMedia(notas)