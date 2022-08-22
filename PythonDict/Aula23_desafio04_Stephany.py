jogador = dict()
gols = []

jogador['nome'] = input("Nome: ")
partidas = int(input("Partidas: "))

for i in range(0,partidas):

    gols.append(int(input("Gols: ")))
jogador['gols']= gols[:]
jogador['total'] = sum(gols)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for x,y in enumerate(jogador['gols']):
    print(f'   => Na partida {x+1}, fez {y} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
