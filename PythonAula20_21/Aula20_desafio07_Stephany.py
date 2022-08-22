maior = 0
menor = 1000

for c in range(1, 6):

    n = int(input('Digite o peso da {} pessoa: '. format(c)))

    if n > maior:
        maior = n
        
    if n < menor:
        menor = n

print('O menor peso é \33[34m{}\33[mKg e o maior peso é \033[31m{}\33[mKg'.format(menor, maior))