<<<<<<< HEAD
numeros=[]

for i in range(30):
    numero=int(input(f"Indique o {i+1}º número: "))
    while numero%2 != 0 or numero < 1 or numero > 50:
        numero=int(input(f"Indique o {i+1}º número: "))
    numeros.append(numero)

=======
numeros=[]

for i in range(30):
    numero=int(input(f"Indique o {i+1}º número: "))
    while numero%2 != 0 or numero < 1 or numero > 50:
        numero=int(input(f"Indique o {i+1}º número: "))
    numeros.append(numero)

>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
print(f"Média= {round((sum(numeros)/len(numeros)), 2)}")