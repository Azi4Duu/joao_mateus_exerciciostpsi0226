<<<<<<< HEAD
# Dicinarios
# {} <--- dicionarios -> tipo de ficheiro json

carros={"Marca" : "BMW", "Modelo" : "M3"}
# acesso em Mapping
# chave - valor

print(carros)
print(carros["Marca"])
print(carros["Modelo"])

#Mudar valor de uma key
carros.update({"Marca" : "Fiat"})
print(carros)

#Adicionar key
carros.update({"Ano" : "2000"})
print(carros)

#Remover key
carros.pop("Ano")
=======
# Dicinarios
# {} <--- dicionarios -> tipo de ficheiro json

carros={"Marca" : "BMW", "Modelo" : "M3"}
# acesso em Mapping
# chave - valor

print(carros)
print(carros["Marca"])
print(carros["Modelo"])

#Mudar valor de uma key
carros.update({"Marca" : "Fiat"})
print(carros)

#Adicionar key
carros.update({"Ano" : "2000"})
print(carros)

#Remover key
carros.pop("Ano")
>>>>>>> ae547a2ce032f2d2508c38f775c151822dc2d86b
print(carros)