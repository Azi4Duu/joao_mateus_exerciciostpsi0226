import re as reg

texto = "Olá,Mundo Mu 4"

lista = reg.split(",", texto)

print(reg.match("Olá", texto))
print(reg.match(r"\d", texto))
print(reg.match("ui", texto))
print(reg.search(r"\d", texto))
var=reg.search("Mu", texto)
var2=reg.findall("Mu", texto)

# * ----> find all
# [A-D]*
# "ABC"
# *.mp3

print(lista)
print(var)
print(var2)

print(type(var))
print(type(var.span))
print(type(var.span()))

print(var.start())
print(var.end())
print(var.span())
print(var.group())
