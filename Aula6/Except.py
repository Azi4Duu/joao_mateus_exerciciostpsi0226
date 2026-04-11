# Exception é um erro que ocorre em runtime e existe uma necessidade de tratar a mesma

#total=10/0 #ZeroDivisionError

#num=int("abc") #ValueError

"""
char=str(1)
print(char)
caracter=chr(1)
print(ord("1"))
print(chr(49))"""

lista = [1,2,3,4]
#print(lista[4]) #IndexError

try:
    total=10/0
except:
    print("Temos um ZeroDivisionError pois não se pode dividir por 0")

string = "Olá mundo"

try:
    result=int(string)
    #print(lista[4])
except ValueError as erroValor:
    print("O erro é",erroValor)
except IndexError as erroIndex:
    print("O erro é",erroIndex)
else:
    print("Não existe error.")

idade = -10

try: 
    if idade<0:
        raise ValueError("Idade não pode ser negativa")
    else:
        print("Idade correcta.")
except ValueError as erroIdade:
    print(erroIdade)
finally:
    print("Fim do programa.")