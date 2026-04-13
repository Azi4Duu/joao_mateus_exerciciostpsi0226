produto = {}

def adicionaElimina(dic:dict):
    dic.update({"Nome" : "Telemóvel", "Preço" : "1500", "Stock" : "30"})
    dic.pop("Stock")

adicionaElimina(produto)
print(produto)