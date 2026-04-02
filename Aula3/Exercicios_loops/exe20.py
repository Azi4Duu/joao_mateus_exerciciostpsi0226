<<<<<<< HEAD
print("\n        MENU")
print("1- Propriedades do nº")
print("2- Calculadora")
opc=int(input("\nEscolha uma opção: "))

match(opc):
    case 1:
        num=int(input("Digite um nº: "))

        while num<1 or num>30000:
            num=int(input("Digite um nº: "))
    
        print()

        contador=0
        for i in range(num,0,-1): # Iteração até ao 1

            primo=True
            perfeito=True
            divisores=0

            if i <= 1:
                primo=False

            for j in range(2, i): # Verifica primos
                if i%j==0:
                    primo=False
                    break
                else:
                    primo=True
                

            soma=0

            for j in range(1,i+1): # Conta divisores e soma para perfeitos
                if i%j==0:
                    divisores+=1
                    soma+=j
                
            if soma-i==i and soma-i!=1:  # Verifica perfeitos
                perfeito=True
            else:
                perfeito=False

            if perfeito:
                if primo:
                    print(f"O nº {i} é primo",end=" ")
                    print(f"| Tem 2 divisores   ",end=" ")
                    print(f"| É perfeito")
                else:
                    print(f"O nº {i} não é primo ",end=" ")
                    print(f"| Tem {divisores} divisores",end=" ")
                    print(f"| É perfeito")
            else:
                if primo:
                    print(f"O nº {i} é primo     ",end=" ")
                    print(f"| Tem 2 divisores",end=" ")
                    print(f"| Não é perfeito")
                else:
                    print(f"O nº {i} não é primo ",end=" ")
                    print(f"| Tem {divisores} divisores",end=" ")
                    print(f"| Não é perfeito")
            
            contador+=1
            
            if contador == 10:
                con=input("Pretende continuar (s/n)? ").lower()
                if con=="s":
                    contador=0
                else:
                    break

    case 2:
        num1=int(input("Digite o primeiro nº: "))

        while num1<1 or num1>1000:
            num1=int(input("Digite o primeiro nº: "))
    
        print()

        print("\n        MENU")
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Tabuada")
        tab=int(input("\nEscolha uma opção: "))
        
        match tab: #Calculadora
            case 1:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} + {num2} = {num1+num2}")
            case 2:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} - {num2} = {num1-num2}")
            case 3:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} x {num2} = {num1*num2}")
            case 4:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} : {num2} = {round((num1/num2), 2)}")
            case 5: #Tabuada até ao numero introduzido
                contador=0
                for i in range(1, num1+1):
                    print(f"{i} x {num1} = {i*num1}")
                    contador+=1
                    if contador == 20:
                        con=input("Pretende continuar (s/n)? ").lower()
                        if con=="s":
                            contador=0
                        else:
=======
print("\n        MENU")
print("1- Propriedades do nº")
print("2- Calculadora")
opc=int(input("\nEscolha uma opção: "))

match(opc):
    case 1:
        num=int(input("Digite um nº: "))

        while num<1 or num>30000:
            num=int(input("Digite um nº: "))
    
        print()

        contador=0
        for i in range(num,0,-1): # Iteração até ao 1

            primo=True
            perfeito=True
            divisores=0

            if i <= 1:
                primo=False

            for j in range(2, i): # Verifica primos
                if i%j==0:
                    primo=False
                    break
                else:
                    primo=True
                

            soma=0

            for j in range(1,i+1): # Conta divisores e soma para perfeitos
                if i%j==0:
                    divisores+=1
                    soma+=j
                
            if soma-i==i and soma-i!=1:  # Verifica perfeitos
                perfeito=True
            else:
                perfeito=False

            if perfeito:
                if primo:
                    print(f"O nº {i} é primo",end=" ")
                    print(f"| Tem 2 divisores   ",end=" ")
                    print(f"| É perfeito")
                else:
                    print(f"O nº {i} não é primo ",end=" ")
                    print(f"| Tem {divisores} divisores",end=" ")
                    print(f"| É perfeito")
            else:
                if primo:
                    print(f"O nº {i} é primo     ",end=" ")
                    print(f"| Tem 2 divisores",end=" ")
                    print(f"| Não é perfeito")
                else:
                    print(f"O nº {i} não é primo ",end=" ")
                    print(f"| Tem {divisores} divisores",end=" ")
                    print(f"| Não é perfeito")
            
            contador+=1
            
            if contador == 10:
                con=input("Pretende continuar (s/n)? ").lower()
                if con=="s":
                    contador=0
                else:
                    break

    case 2:
        num1=int(input("Digite o primeiro nº: "))

        while num1<1 or num1>1000:
            num1=int(input("Digite o primeiro nº: "))
    
        print()

        print("\n        MENU")
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Tabuada")
        tab=int(input("\nEscolha uma opção: "))
        
        match tab: #Calculadora
            case 1:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} + {num2} = {num1+num2}")
            case 2:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} - {num2} = {num1-num2}")
            case 3:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} x {num2} = {num1*num2}")
            case 4:
                num2=int(input("Digite o segundo nº: "))

                while num2<1 or num2>1000:
                    num2=int(input("Digite o segundo nº: "))

                print(f"{num1} : {num2} = {round((num1/num2), 2)}")
            case 5: #Tabuada até ao numero introduzido
                contador=0
                for i in range(1, num1+1):
                    print(f"{i} x {num1} = {i*num1}")
                    contador+=1
                    if contador == 20:
                        con=input("Pretende continuar (s/n)? ").lower()
                        if con=="s":
                            contador=0
                        else:
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
                            break