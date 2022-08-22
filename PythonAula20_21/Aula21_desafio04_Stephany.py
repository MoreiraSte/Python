total = totmil = menor = cont =0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco

    if preco > 1000:
        totmil  += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '

    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra for \33[31mR${total:.2f}\33[m')
print(f'Temos \33[32m{totmil}\33[m produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \33[33m{barato} que custa R${menor:.2f}\33[m')