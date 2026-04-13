<<<<<<< HEAD
numeros=[]
pares=[]
impares=[]

for i in range(1,11):
    numeros.append(int(input(f"Indique o {i}º Número: ")))
    if numeros[i-1]%2 == 0:
        pares.append(numeros[i-1])
    else:
        impares.append(numeros[i-1])


print("\nNúmeros:", end=" ")
for i in range(len(numeros)):
    print(f"{numeros[i]}", end=" ")

print("\nPares:", end=" ")
for i in range(len(pares)):
    print(f"{pares[i]}", end=" ")

print("\nImpares:", end=" ")
for i in range(len(impares)):
=======
numeros=[]
pares=[]
impares=[]

for i in range(1,11):
    numeros.append(int(input(f"Indique o {i}º Número: ")))
    if numeros[i-1]%2 == 0:
        pares.append(numeros[i-1])
    else:
        impares.append(numeros[i-1])


print("\nNúmeros:", end=" ")
for i in range(len(numeros)):
    print(f"{numeros[i]}", end=" ")

print("\nPares:", end=" ")
for i in range(len(pares)):
    print(f"{pares[i]}", end=" ")

print("\nImpares:", end=" ")
for i in range(len(impares)):
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
    print(f"{impares[i]}", end=" ")