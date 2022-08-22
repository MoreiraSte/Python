lista = []
listaP = []
listaI = []

while True:
    n = int(input("Digite um numero: "))
    resp = str(input("Deseja continuar? [S/N]: "))

    lista.append(n)

    if n % 2 ==0:
        listaP.append(n)
    else:
        listaI.append(n)

    if resp in 'Ss':
        continue
    elif resp in 'Nn':
        break

print(f'Lista: {lista}')
print(f'Pares: {listaP}')
print(f'Impares: {listaI}')