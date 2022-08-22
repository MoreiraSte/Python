listanum = []
maior = 0
menor=0

for x in range (0,5):
    listanum.append(int(input(f'Digite um numero na posição \33[31m{x}\33[m° : ')))

    if x == 0:
        maior= menor= listanum[x]
    else:
        if listanum[x] > maior:
            maior = listanum[x]
        if listanum[x] < menor:
            menor = listanum[x]

print(f'Lista: {listanum}')
print(f'Maior: {maior} nas posições ',end='')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i} , ',end='')

print("\n")
print(f'Menor: {menor} nas posições ',end='')

for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i} , ',end='')
