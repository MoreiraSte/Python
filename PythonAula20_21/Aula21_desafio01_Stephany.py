print('TABUADA')

while True:

    n = int(input('digite um número: '))

    if n < 0:
        break

    for d in range(1, 11):
        print(f'{n} x {d} = {n*d}')

print('FIM')