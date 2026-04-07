import os

alunos = []

def inserir(lista):

    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")

    aluno = {"Nome" : nome, "Idade" : idade, "Curso" : curso}
    lista.append(aluno)


while True:

    os.system("cls")

    print("MENU")
    print("1- Inserir")
    print("2- Listar")
    print("3- Sair")

    opt = input("Insira uma opção: ")

    match opt :
        case "1":
            os.system("cls")
            inserir(alunos)
        case "2":
            os.system("cls")
            for aluno in alunos:
                print("-----------------------")
                print(f"Nome: {aluno["Nome"]}")
                print(f"Idade: {aluno["Idade"]}")
                print(f"Curso: {aluno["Curso"]}")
            input()
        case "3":
            break
        case _:
            os.system("cls")
            print("Não inseriste uma opção válida!")
            print("Pressiona ENTER para voltar.")
            input()


