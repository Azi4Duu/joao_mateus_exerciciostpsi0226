<<<<<<< HEAD
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
=======
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
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
    print("Não é número primo")