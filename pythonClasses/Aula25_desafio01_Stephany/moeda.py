class Calculos:
    def __init__(self,valor,tx):
        self.valor = valor
        self.tx = tx



def aumentar(valor,tx):
    print(f'Valor aumentao em \33[31m{tx:.0f}%\33[m : R${valor + tx}')

def diminuir(valor,tx):
    print(f'Valor diminuindo em \33[34m{tx:.0f}%\33[m : R${valor - tx}')

def dobro(valor):
    print(f'Dobro: R$ {valor * 2}')


def metade(valor):
    print(f'Metade: R$ {valor / 2}')