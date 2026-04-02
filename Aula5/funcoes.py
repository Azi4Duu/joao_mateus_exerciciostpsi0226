# é um bloco de codigo isolado que pode ser chamdo varias vezes
# dado pertencer a um bloco de codigo pequeno, torna -se mais facil a sua manutenção 
# em segurança no scope, quando bem aplicada
# scopes e manipulação são feitos atraves de passagem da valores/parametros e passagem das referencias das variaveis

num1=12
num2=13

# valorDeRetorno nomeDaFunc (parametros de entrada)


def troca(n1, n2):
    #troc = 0
    #troc = n1
    #n1 = n2
    #n2 = troc

    n1, n2 = n2, n1
    return n1, n2

num1, num2 = troca(num1, num2)
print("\nnum 1:", num1, "num 2:", num2)

lista1=[12,13,14]

print("\nlista antes da função:", lista1)

def insertValue(lista):
    lista.append(19)

insertValue(lista1)

print("lista depois da função:", lista1)
