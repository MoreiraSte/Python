lista = list()
mulheres = list()
dicionario = dict()
soma = 0

while True:
    dicionario.clear()
    dicionario['Nome'] = str(input('Nome: ')).strip()
    dicionario['Idade'] = int(input('Idade: '))

    while True:
        dicionario['Sexo:'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if dicionario['Sexo:'] in 'MF':
            break
        print('Opção Inválida!')

    lista.append(dicionario.copy())
    soma += dicionario['Idade']

    if dicionario['Sexo:'] == 'F':
        mulheres.append(dicionario['Nome'])

    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
    if op == 'N':
        break


print(f'''A) Total de pessoas cadastradas: {len(lista)}
B) Média de idade: {soma/len(lista):.2f}
C) Mulheres cadastradas {mulheres}
D) Pessoas com idade acima da média: ''')

for a in lista:
    if a['Idade'] >= soma/len(lista):
        print(f'   {a["Nome"]}: {a["Idade"]}')