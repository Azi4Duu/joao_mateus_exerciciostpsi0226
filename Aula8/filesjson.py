import os
import json

filename = "./Aula8/Dados/data2.txt"


if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        dicionario=json.load(manipfile)
else:
    dicionario={}


dicionario={"nome" : "João", "tel" : 2}

with open(filename, "w", encoding="utf-8") as manipfile:
    json.dump(dicionario, manipfile, ensure_ascii= True, indent="   ")