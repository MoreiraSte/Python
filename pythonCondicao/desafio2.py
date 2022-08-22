vel = int(input("Digite a velociade (francesssssscooooooo) do carro: "))
vm = (vel-80)*7
if (vel > 80):
    print(f'Sua velocidade é {vel}, por isso você foi multado')
    print(f'Valor da multa é de: R$ {vm}')
else:
    print("Você está no limite (katchau)")