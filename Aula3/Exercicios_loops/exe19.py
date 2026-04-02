cont=0
soma=0
ant=1
ant2=1

while cont < 60:
    print(ant)
    soma=ant+ant2
    ant2=ant
    ant=soma
    cont+=1