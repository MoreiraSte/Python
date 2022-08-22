import random
from time import sleep


def sorteia():
    numeros = []
    for i in range(5):
        sorteado = random.randint(1,10)
        sleep(0.5)
        numeros.append(sorteado)
    return numeros

def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print("A soma dos numeros da lista {} eh: {}".format(numeros, soma))



if __name__ == '__main__':
    somaPar(sorteia())