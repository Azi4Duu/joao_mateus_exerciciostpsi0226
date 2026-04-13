def aceder(base:dict):
    return base["Modelo"]

carros = {"Marca" : "Toyota", "Modelo" : "Corolla", "Ano" : "2020"}

print(aceder(carros))