quantMaior = quantHomens = quantMulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        quantMaior += 1

    if sexo == 'M':
        quantHomens += 1
    elif idade < 20:
        quantMulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'''
Maiores de idade cadastrados: {quantMaior}
Homens cadastrados: {quantHomens}
Mulheres com idade inferior a 20: {quantMulheres}
''')