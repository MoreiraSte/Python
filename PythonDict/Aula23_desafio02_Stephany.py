import random

valores = dict()
dados = []

valores['jogador1'] = random.randint(1,6)
valores['jogador2'] = random.randint(1,6)
valores['jogador3'] = random.randint(1,6)
valores['jogador4'] = random.randint(1,6)

dados.append(valores.copy())

for i, j in valores.items():

    print(f'O {i} sorteou {j}\n',end=' ')
