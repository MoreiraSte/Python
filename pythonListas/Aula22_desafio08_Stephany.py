lista = []
listaP = []
listaI = []

for i in range(0,8):
    n = int(input("Digite um numero: "))
    resp = str(input("Deseja continuar? [S/N]: "))

    lista.append(n)

    if n % 2 ==0:
        listaP.append(n)
        listaP.sort()
    else:
        listaI.append(n)
        listaI.sort()


    if resp in 'Ss':
        continue
    elif resp in 'Nn':
        break


print(f'Pares: {listaP}')
print(f'Impares: {listaI}')