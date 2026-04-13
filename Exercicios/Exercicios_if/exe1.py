seg = 0
horas = 0
minutos = 0
segundos = 0

seg = int(input("Indique a quantidade de segundos pretendida: "))

if seg >= 3600:
    horas = int(seg / 3600)
    seg = seg % 3600

if seg >= 60:
    minutos = int(seg / 60)
    seg = seg % 60

segundos = seg

print(f"{horas} horas, {minutos} minutos e {segundos} segundos ")


