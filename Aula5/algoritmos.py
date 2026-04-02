nomes=["do", "re", "mi", "do"]
ind=[]

def insert(nomesinsert:list):
    nomesinsert.append(input("Insere um nome: "))

def listar(nomeslist:list):
    for nome in nomeslist:
        print("Nome:", nome)

def delete(nomesdelete:list, indices:list):
    if len(indices) > 0 :
        for i in indices:
            resp = input(f"Pretende apagar o nome no indice {i} (s/n)?")
            if resp.lower() == "s" :
                nomesdelete.pop(i)
    else : 
        nomesdelete.pop(int(input("Insere uma posição: ")))
    
    indices.clear()

def procurar(nomesprocura:list, indices:list):
    indices.clear()
    nome = input("Insere um nome: ")
    for i in range(len(nomesprocura)):
        if nomesprocura[i] == nome:
            indices.append(i)
    
    #return(indices)

while True:
    print("1- Inserir nome")
    print("2- Listar nomes")
    print("3- Eliminar nome")
    print("4- Procurar nome")
    print("5- Sair")

    opt = input("Escolha uma opção: ")

    match opt:
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes, ind)
        case "4":
            print(f"Posições: {ind}")
        case "5":
            print("Fim do programa!")
            break
        case _:
            print("Não escolheu uma opção válida")