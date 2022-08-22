import random


def gera():
    return random.randint(0, 10)


def game():
    resposta = gera()
    tentativa = 0
    chute = 0

    print("O computador irá sortear um número entre 0 e 10, descubra....: ")

    while chute is not resposta:

        chute = int(input("Dê um palpite de 0 a 10: "))

        tentativa +=  1

        if chute == resposta:
            print("Você palpitou {} vezes".format(tentativa))
            break




game()