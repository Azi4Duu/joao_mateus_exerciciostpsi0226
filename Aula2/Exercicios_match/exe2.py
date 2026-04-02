nota=int(input("Indique a classificação: "))

if nota >= 90:
    opc=1
elif nota >= 70:
    opc=2
elif nota >= 50:
    opc=3
else:
    opc=4

match opc:
    case 1:
        print("Excelente")
    case 2:
        print("Bom")
    case 3:
        print("Suficiente")
    case 4:
        print("Insuficiente")