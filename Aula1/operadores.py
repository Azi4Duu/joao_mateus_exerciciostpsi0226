#operadores aritemeticos

# soma +, sub -, div /, mult *, mode %, exponencial **

total=0
num1=0
num2=0

#input
num1=int(input("Insira o 1º numero: "))
num2=int(input("Insira o 2º numero: "))

total=num1+num2
print(f"soma: {total}")

total=num1-num2
print("sub: ", total, " .")

total=num1*num2
print(f"mult: {total}")

total=num1/num2
print("div: ", total, " .")

# operadores de controlo de decisão

# == igualdade, != diferente, > maior que, < menor que,
#  >= maior ou igual, <= menor ou igual

# expressão
# Val1 == Val2 = True/False

# operadores logicos
# and e o or

# expressão
# Val1 > Val2 and Val2 > Val3 = True/False
#    true     and    false    = False

# If

#--------------------------------------#
# exercicio encontra o maior e o menor #
#--------------------------------------#

val1=2
val2=3
val3=4

if val1>val2 and val1>val3:
    if val2>val3:
        print("Val1 é o maior e Val3 o menor")
    else:
        print("Val1 é o maior e Val2 o menor")
elif val2>val1 and val2>val3:
    if val1>val3:
        print("Val2 é o maior e Val3 o menor")    
    else:
        print("Val2 é o maior e Val1 o menor")
elif val3>val1 and val3>val2:
    if val1>val2:
        print("Val3 é o maior e Val2 o menor")    
    else:
        print("Val3 é o maior e Val1 o menor")

if val1>val2 and val2>val3:
    print("Val1 é o maior e Val3 o menor")
elif val1>val3 and val3>val2:
    print("Val1 é o maior e Val2 o menor")
elif val2>val3 and val3>val1:
    print("Val2 é o maior e Val1 o menor")
elif val2>val1 and val1>val3:
    print("Val2 é o maior e Val3 o menor")
elif val3>val1 and val1>val2:
    print("Val3 é o maior e Val2 o menor")
else:
    print("Val3 é o maior e Val1 o menor")


# match case/switch case

opc=1

print("Prima 1 para bom dia")
print("Prima 2 para boa tarde")
print("Prima 3 para sair")

opc=input("Escolha a opcao: ")

match opc:
    case "1":
        print("Bom dia")
    case "2":
        print("Boa tarde")
    case "3":
        print("Sair do programa")
    case _:
        print("Erro")
