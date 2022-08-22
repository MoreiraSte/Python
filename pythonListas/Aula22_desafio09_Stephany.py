matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range (0,3):
        for x in range(0,3):
            matriz[i][x] = int(input(f'Digite um valor para [{i},{x}]: '))



for i in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[i][x]:^5}]',end='')
    print ()