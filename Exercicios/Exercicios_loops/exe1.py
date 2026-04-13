<<<<<<< HEAD
pares=""
impares=""

for i in range(1,31):
    print(f"{i}", end=" ")
    if (i%2)==0:
        pares=f"{pares} {i}"
    else:
        impares=f"{impares} {i}"

print(f"\nPares:{pares}")
=======
pares=""
impares=""

for i in range(1,31):
    print(f"{i}", end=" ")
    if (i%2)==0:
        pares=f"{pares} {i}"
    else:
        impares=f"{impares} {i}"

print(f"\nPares:{pares}")
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
print(f"Impares:{impares}")