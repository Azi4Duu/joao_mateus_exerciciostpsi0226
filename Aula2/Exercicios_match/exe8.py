operacao=input("Operação: ").lower()
num1=int(input("Número 1: "))
num2=int(input("Número 2: "))

match operacao:
    case op if op == "divide":
        print(round((num1/num2), 1))
    case op if op == "subtrai":
        print(num1-num2)
    case op if op == "soma":
        print(num1+num2)
    case op if op == "multiplica":
        print(num1*num2)
