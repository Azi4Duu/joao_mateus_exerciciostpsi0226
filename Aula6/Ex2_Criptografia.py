mensagem = input("Introduza a mensagem: ")
chave = input("Introduza a chave para criptografar: ")
while len(chave) == 0:
    print("Tem de introduzir uma chave!")
    chave = input("Introduza a chave para criptografar: ")

def criptografar(msg:str, chv:str):
    msgCrypt = []
    soma = 0
    for letra in chv:
        soma += ord(letra)
    
    for letra in msg:
        nova = 32 + ((ord(letra) - 32 + soma) % 95)
        msgCrypt.append(nova)
    
    return msgCrypt

def descriptografar(codigos:list[int], chvCrypt:str):
    soma = 0
    mxg = ""

    for letra in chvCrypt:
        soma += ord(letra)

    for codigo in codigos:
         original = 32 + ((codigo - 32 - soma) % 95)
         mxg += chr(original)
    
    return mxg

print(criptografar(mensagem, chave))
print(descriptografar(criptografar(mensagem, chave), chave))