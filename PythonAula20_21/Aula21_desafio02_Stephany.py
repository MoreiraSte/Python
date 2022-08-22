from random import randint
v = 0
while True:
    opcao = ' '
    while opcao not in 'pi':
        opcao = str(input('Você quer par ou ímpar? (P/I) ')).lower().strip()[0]
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if opcao in 'p':
        if total % 2 == 0:
            print('\033[1;32mVOCÊ GANHOU! Vamos continuar.\033[m')
            v += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
    if opcao in 'i':
        if total % 2 == 1:
            print('\033[1;32mVOCÊ GANHOU! Vamos continuar.\033[m')
            v += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
print(f'\033[1;35mACABOU!\033[m Você venceu {v} vezes')