jogador1=input("Jogador1: ")
jogador2=input("Jogador2: ")

jogada=[jogador1, jogador2]

match jogada:
    case j if (j[0] == "pedra" and j[1] == "tesoura") or (j[0] == "tesoura" and j[1] == "papel") or (j[0] == "papel" and j[1] == "pedra"):
        print("Jogador1 venceu!")
    case j if (j[0] == "tesoura" and j[1] == "pedra") or (j[0] == "papel" and j[1] == "tesoura") or (j[0] == "pedra" and j[1] == "papel"):
        print("Jogador2 venceu!")
    case j if j[0] == j[1]:
        print("Empate!")
