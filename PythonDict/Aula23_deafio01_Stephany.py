media = dict()
situacao = []

media['nome'] =input("Digite seu nome: ")
media['media'] = float(input("Digite sua média: "))
situacao.append(media.copy())

if media['media'] > 0 and media['media'] < 3.9:

    media['situacao'] = 'Reprovado'

elif media['media'] > 4 and media['media'] < 6.9:
    media['situacao'] = 'Recuperação'

elif media['media'] > 7 and media['media'] < 10:

    media['situacao'] = 'Aprovado'

for i, k in media.items():
    print(f'{i} é igual a {k}\n', end=' ')
