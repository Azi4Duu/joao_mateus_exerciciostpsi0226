# loops For // While

nomes=["João", "Pedro", "Maria"]
#index    0       1        2

for nome in nomes:
    print(nome)

# função range()

for i in range(3):
    print(nomes[i])

for i in range(len(nomes)):
    print(nomes[i])

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

# while <--- controlado por uma expressão ex: Val1 < Val2

i=0

while i < len(nomes):
    print(nomes[i])
    i+=1

while True:
    print("1- Bom dia")
    print("2- Boa tarde")
    print("3- Sair")

    opc=input("Indique a opc:")

    match opc:
        case "1":
            print("bom dia")
        case "2":
            print("bom dia")
        case "3":
            print("sair")
            break
        case _:
            print("opc errada")