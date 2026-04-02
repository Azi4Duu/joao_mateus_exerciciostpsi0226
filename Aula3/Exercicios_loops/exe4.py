num=int(input("Indique um número: "))

primo=1

if num <= 1:
    primo=0
else:
    for i in range (2, num):
        if num%i == 0:
            primo=0
            break
        else:
            primo=1

if primo == 1 :
    print("É número primo")
else:
    print("Não é número primo")