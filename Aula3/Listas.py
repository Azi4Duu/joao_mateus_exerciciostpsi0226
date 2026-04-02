#Listas em inteiros

numeros=[1,5,8,3,9,23]
#index   0 1 2 3 4 5

for numero in numeros:
    print(numero)

numeros[2]=6

for numero in numeros:
    print(numero)

#Listas de strings

#ind D1   0       1        2
nomes=["João", "Pedro", "Maria"]
#ind D2 0123    01234    01234

for nome in nomes:
    print(nome)

#print("ola","mundo",end="\t",sep="     ")
print("",end="\n\n\n")
print(nomes[0])

nomes[0]="Tiago"
print(nomes[0])
print(nomes[0][2])

# 1- Quantas dimenções realmente tem?
# 2- Como adicionar mais elementos?
# 3- Como remover elementos?
# 4- == compara unicode da string completa

print(nomes)

nomes.remove("Pedro") #Não se pode falhar
print(nomes)

nomes.pop(0) #tambem remove, mas por posição 
print(nomes)

nomes.append("João Mateus") #adiciona no fim da lista
print(nomes)
print(nomes.count("Maria")) #conta quantos elementos("Maria") há

print(nomes)
print(len(nomes))
print(nomes.index("João Mateus")) #Indica a posição do elemento pretendido

