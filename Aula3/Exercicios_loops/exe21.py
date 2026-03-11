import os

base=[]
numcli=1
num=int(input("Quantos clientes pretende introduzir? "))

for i in range(num):

    nomcli=input("Nome do cliente: ")
    while len(nomcli)==0:
        nomcli=input("Nome do cliente: ")
    
    morada=input("Morada: ")
    while len(morada)==0:
        morada=input("Morada: ")
    
    telemovel=input("Nº Telemovel: ")
    while len(telemovel)==0 or len(telemovel)!=9 or not telemovel.isnumeric():
        telemovel=input("Nº Telemovel: ")
    
    nif=input("NIF: ")
    while len(nif)==0 or len(nif)!=9 or not nif.isnumeric():
        nif=input("NIF: ")
    
    compra=input("Valor da compra: ")
    while not compra.isnumeric():
        compra=input("Valor da compra: ")
    
    while int(compra)<=0:
        compra=int(input("Valor da compra: "))
    
    desconto=0
    if int(compra) > 500:
        desconto=int(compra)*0.15
    elif int(compra) > 200:
        desconto=int(compra)*0.1
    elif int(compra) > 100:
        desconto=int(compra)*0.05
    
    divfin=int(compra)-desconto

    cliente={"NumCli" : numcli, "NomCli" : nomcli, "Morada" : morada, "Tel" : telemovel, "NIF" : nif, "Compra" : compra, "Divfin" : divfin}
    base.append(cliente)
    numcli+=1
    os.system("cls")

while True:

    print("         MENU")
    print("1- Listagem dos clientes")
    print("2- Procurar um cliente")

    opc=int(input("\nEscolha uma opção: "))
    while opc!=1 and opc!=2:
        opc=int(input("\nEscolha uma opção: "))

    os.system("cls")

    match opc:
        case 1:
            for i in range(len(base)):
                print(base[i])
        case 2:
            ncli=int(input("Nº do Cliente: "))
            while ncli>(len(base)+1) or ncli<1:
                ncli=int(input("Nº do Cliente: "))
            for i in range(len(base)):
                if base[i]["NumCli"] == ncli:
                    print(base[i])
    
    voltar=input("Pretende voltar ao MENU (s/n)? ")
    if voltar == "s":
        os.system("cls")
    elif voltar == "n":
        break 
                

    
