rep=int(input("Indique quantos nºs pretende apresentar: "))
cont=0

for i in range(rep):
    if i==0:
        num=int(input("Introduza um nº: "))
    else:
        num=int(input("\nIntroduza um nº: "))
    
    soma=0

    for j in range(1,num):
        if num%j==0:
            soma+=j

    if soma==num:
        cont+=1
        print(f"O nº {num} é perfeito.")
        print(f"{num}=",end="")
        for j in range (num-1,0,-1):
            if num%j==0 and j > 1:
                print(f"{j}+",end="")
            elif j==1:
                print(f"{j}",end="")
    else:
        print(f"O nº {num} não é perfeito.",end="")

print(f"\n\nIntroduziu {cont} nºs perfeitos.")
