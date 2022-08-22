quilometros = float(input("Digite os quilometos percorridos pelo carro: "))
dias = int(input("Digite a quantidade de dias pelos quais foi alugado: "))

preco = (quilometros*0.15) + (dias*60.00)

print(f'o preço a pagar é {preco}')