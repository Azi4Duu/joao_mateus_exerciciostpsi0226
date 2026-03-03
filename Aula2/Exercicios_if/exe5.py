num1=0
num2=0
num3=0

num1=int(input("Indique o primeiro nº: "))
num2=int(input("Indique o segundo nº: "))
num3=int(input("Indique o terceiro nº: "))

if num1 > num2 and num2 > num3:
    print(f"Crescente: {num3}, {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}, {num3}")
elif num1 > num3 and num3 > num2:
    print(f"Crescente: {num2}, {num3}, {num1}")
    print(f"Decrescente: {num1}, {num3}, {num2}")
elif num2 > num1 and num1 > num3:
    print(f"Crescente: {num3}, {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}, {num3}")
elif num2 > num3 and num3 > num1:
    print(f"Crescente: {num1}, {num3}, {num2}")
    print(f"Decrescente: {num2}, {num3}, {num1}")
elif num3 > num1 and num1 > num2:
    print(f"Crescente: {num2}, {num1}, {num3}")
    print(f"Decrescente: {num3}, {num1}, {num2}")
elif num3 > num2 and num2 > num1:
    print(f"Crescente: {num1}, {num2}, {num3}")
    print(f"Decrescente: {num3}, {num2}, {num1}")