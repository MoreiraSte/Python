
num = (int(input('1º valor:')), int(input('2º valor:')), int(input('3º valor:')), int(input('4º valor:')), int(input('5º valor:')), int(input('6º valor:')))
print(f'Tupla: {num}')

print(f'O número 9 aparece {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado')
print('Números pares digitados: ', end='')

for i in num:
    if i % 2 == 0:
        print(i, end=' ')