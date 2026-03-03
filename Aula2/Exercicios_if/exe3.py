num1=0
num2=0

num1=int(input("Indique o primeiro nº: "))
num2=int(input("Indique o segundo nº: "))

if num1 > num2:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")
else:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")