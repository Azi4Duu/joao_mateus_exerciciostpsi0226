saldo=0
cheque=0

saldo=float(input("Indique o saldo: "))
cheque=float(input("Indique o valor do cheque: "))

if saldo >= cheque:
    print(f"Cheque descontado, saldo: {saldo-cheque}")
else:
    print("Não possui saldo suficiente!")
    print("Não foi possível descontar o cheque!")