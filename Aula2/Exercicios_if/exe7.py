nota1 = float(input("Indique a nota da primeira prova: "))
nota2 = float(input("Indique a nota da segunda prova: "))
nota3 = float(input("Indique a nota da terceira prova: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print("Média:", round(media, 1))

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")