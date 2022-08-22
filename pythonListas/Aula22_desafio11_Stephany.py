import random
lista= list()
jogo = list()
qts = int(input("Quantos jogos voce quer? "))
total = 1

while total <= qtd:
    cont = 0
    while True:
        numeros = random.randint(1,60)
        if numeros not in lista:
                lista.append(numeros)
                cont+=1
        if cont >= 6:
            break

    list.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1
for i,j in enumerate (jogo):
    print("jogo ",i+1,":",j)