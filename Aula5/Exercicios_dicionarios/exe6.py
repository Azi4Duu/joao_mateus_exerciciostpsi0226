vendas = {"Janeiro" : 1000, "Fevereiro" : 1500, "Março" : 1200}

def somaMeses(dic:dict):
    soma = 0
    for mes in dic:
        soma += dic[mes]
    return soma

print(somaMeses(vendas))