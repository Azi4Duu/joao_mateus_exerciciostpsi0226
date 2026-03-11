notas=[]

for i in range(10):
    notas.append(int(input(f"Indique a nota do {i+1}º aluno: ")))

print(f"\nMedia= {sum(notas)/len(notas)}")