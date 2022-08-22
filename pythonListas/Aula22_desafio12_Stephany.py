ficha = list()
while True:
    nome = input("Nome:  ")
    n1 = float(input("Nota 1:  "))
    n2 = float(input("Nota 2:  "))
    media = (n1+n2)/2
    ficha.append([nome,[n1,n2],media])

    resp = input("Quer continuar? [S/N]:  ")

    if resp in 'Nn':
        break

print(f'{"No.":<4}{"Nome":<10}{"média":>8}')

for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    op = int(input("Mostrar notas de qual aluno: [999 para parar]:  "))
    if op == 999:
        print("Finalizado")
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
print("Fim....")