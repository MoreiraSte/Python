import random

alunos = []

for i in range(4):
    aluno =input(f'Digite o nome do aluno{i+1}: ')
    alunos.append(aluno)

print(f'O aluno sorteado foi:{alunos[random.randint(0,3)]}')