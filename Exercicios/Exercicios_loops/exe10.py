<<<<<<< HEAD
numero=int(input("Indique um número: "))
divisores=0

for i in range(1,numero+1):
    if numero%i==0:
        divisores+=1

=======
numero=int(input("Indique um número: "))
divisores=0

for i in range(1,numero+1):
    if numero%i==0:
        divisores+=1

>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
print(f"O número {numero} tem {divisores} divisores.")