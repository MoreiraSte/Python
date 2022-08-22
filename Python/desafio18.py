import random

alunos = []

for i in range(4):
    aluno =input(f'Digite o nome do aluno{i+1}: ')
    alunos.append(aluno)

    alunos.sort()

print(f'A ordem de alunos é: {alunos}')