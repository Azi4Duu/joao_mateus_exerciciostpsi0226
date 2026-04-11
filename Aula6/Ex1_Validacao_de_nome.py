nome = input("Escreva o seu nome: ")

def validaNome(n:str):
     if len(n) == 0:
          return False
     elif not (65 <= ord(n[:1]) <= 90):
          return False
     
     i=0
     for letra in n:
          if not(65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122 or ord(letra) == 32):
               return False
          if ord(letra) == 32:

            if i + 1 < len(n):
                if not (65 <= ord(n[i + 1]) <= 90):
                    return False
          i += 1          

if validaNome(nome):
    print("Nome válido!")
else:
    print("Nome inválido: contém caracteres não permitidos.")