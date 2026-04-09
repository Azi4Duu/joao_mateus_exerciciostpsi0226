palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

def ordenaPalavras(pal:list):
    for i in range(len(pal)):
        for j in range(len(pal)):
            if j < len(pal) - 1:
                if ord(((pal[j])[:1]).lower()) < ord(((pal[j+1])[:1]).lower()):
                    pal[j+1], pal[j] = pal[j], pal[j+1] 

ordenaPalavras(palavras)
print(palavras)