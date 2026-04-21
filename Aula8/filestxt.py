import pathlib

# qualquer ação com ficheiros
# read, write, append, binario
# 1 - open file
# 2 - ação
# 3 - close file

filename="./Aula8/Dados/data.txt"

if pathlib.Path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        texto=manipfile.read()
    print("no file:", texto)
else:
    texto=input("Escreva uma frase: ")

    with open(filename, "w", encoding="utf-8") as manipfile:
        manipfile.write(texto)
