matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar=0
soma=0
maior=0
for i in range (0,3):
        for x in range(0,3):
            matriz[i][x] = int(input(f'Digite um valor para [{i},{x}]: '))

for i in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[i][x]:^5}]',end='')
        if matriz[i][x] % 2 == 0:
            somaPar += matriz[i][x]
    print ()
    print(f'A soma dos valores pares é{somaPar}')

for i in range(0,3):
    soma += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {soma}')
for x in range(0,3):
    if x ==0:
        maior = matriz[1][x]
    elif matriz[1][x] > maior:
        maior = matriz[1][x]
print(f'O maior valor da segunda linha é {maior}')

