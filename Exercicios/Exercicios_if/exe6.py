total=0
desconto=0
nome=input("Indique o nome do cliente: ")
valor=float(input("Indique o valor da compra: "))

if valor <= 200:
    desconto = float(valor * 0.1)
    total = valor - (desconto)
elif valor <= 500:
    desconto = float(valor * 0.15)
    total = valor - (desconto)
else:
    desconto = float(valor * 0.2)
    total = valor - (desconto)

print(f"Nome: {nome}")
print(f"Compra: {valor}")
print(f"Desconto: {desconto}")
print(f"Total a pagar: {total}")