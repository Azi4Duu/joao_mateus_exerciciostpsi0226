cont=0

for i in range(1, 256):
    print(f"{i}-{chr(i)}")
    cont+=1
    if cont==20:
        opc=input("Pretende continuar (s/n)? ").lower()
        if opc=="n":
            break
        else:
            cont=0