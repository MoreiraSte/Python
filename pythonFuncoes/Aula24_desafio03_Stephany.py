from time import sleep

def contador(i, f, p):

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='|')
            cont += p
            sleep(0.5)
        print('')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='|')
            cont -= p
            sleep(0.4)
        print('')

if __name__=='__main__':
    contador(1,10,1)
    contador(10,0,2)
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    contador(inicio, fim, passo)