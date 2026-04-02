pares=""
impares=""

for i in range(1,31):
    print(f"{i}", end=" ")
    if (i%2)==0:
        pares=f"{pares} {i}"
    else:
        impares=f"{impares} {i}"

print(f"\nPares:{pares}")
print(f"Impares:{impares}")