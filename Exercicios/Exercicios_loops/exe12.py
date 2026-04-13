<<<<<<< HEAD
numero=int(input("Indique um numero: "))
operacoes=0

print("\nMULTIPLICAÇÃO")
for i in range(1, numero+1):
    print(f"{numero} x {i} = {numero*i}")
    operacoes+=1

print("\nDIVISÃO")
for i in range(1, numero+1):
    print(f"{numero} : {i} = {round((numero/i), 2)}")
    operacoes+=1

print("\nSOMA")
for i in range(1, numero+1):
    print(f"{numero} + {i} = {numero+i}")
    operacoes+=1

print("\nSUBTRAÇÃO")
for i in range(1, numero+1):
    print(f"{numero} - {i} = {numero-i}")
    operacoes+=1

=======
numero=int(input("Indique um numero: "))
operacoes=0

print("\nMULTIPLICAÇÃO")
for i in range(1, numero+1):
    print(f"{numero} x {i} = {numero*i}")
    operacoes+=1

print("\nDIVISÃO")
for i in range(1, numero+1):
    print(f"{numero} : {i} = {round((numero/i), 2)}")
    operacoes+=1

print("\nSOMA")
for i in range(1, numero+1):
    print(f"{numero} + {i} = {numero+i}")
    operacoes+=1

print("\nSUBTRAÇÃO")
for i in range(1, numero+1):
    print(f"{numero} - {i} = {numero-i}")
    operacoes+=1

>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
print(f"\nForam efetuadas {operacoes} operações.")