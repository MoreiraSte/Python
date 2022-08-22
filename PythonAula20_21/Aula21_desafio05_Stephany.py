ced = 50.00
cedTotal = 0

print("Cédulas disponíveis R$50, R$20, R$10 e R$1")
sacar = int(input('Qual valor você deseja sacar? R$'))

while True:
    if sacar >= ced:
        sacar -= ced
        cedTotal += 1
    else:
        if cedTotal != 0:
            print(f'Total de {cedTotal} de R${ced:.2f}')
        if ced == 50.00:
            ced = 20.00
        elif ced == 20.00:
            ced = 10.00
        elif ced == 10.00:
            ced = 1
        cedTotal = 0
        if sacar == 0:
            break