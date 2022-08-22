dis = int(input("Digite a distância em Km da viagem: "))

if dis <= 200:
    valor = dis* 0.50
    print(f'O custo da viagem será de R$ {valor}')
else:
    valor1 = dis*0.45
    print(f'O custo da viagem será de R$ {valor1}')