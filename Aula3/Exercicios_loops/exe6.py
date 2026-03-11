primos=[]
primo=True

for i in range(2, 10):
    for j in range (2, i):
        if i%j == 0:
            primo=False
            break
        else:
            primo=True

    if primo:
        primos.append(i)

print(f"Nºs primos: {primos}")
        