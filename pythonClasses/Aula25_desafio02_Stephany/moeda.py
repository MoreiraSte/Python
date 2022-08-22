class Calculos:
    def __init__(self,valor,tx,preco,moeda):
        self.valor = valor
        self.tx = tx
        self.preco = preco
        self.moeda = moeda



# def aumentar(valor,tx):
#     print(f'Valor aumentao em \33[31m{tx:.0f}%\33[m : R${valor + tx}')
#
# def diminuir(valor,tx):
#     print(f'Valor diminuindo em \33[34m{tx:.0f}%\33[m : R${valor - tx}')


def moeda(preco,moeda,tx):
    precovirgula = str(preco).replace(".", ",")
    conta1 = preco + tx
    conta1 = str(conta1).replace(".", ",")
    conta2 = preco - tx
    conta2 = str(conta2).replace(".", ",")
    print(f'Valor aumentado de \033[33m{moeda}{precovirgula}0\033[m com taxa de \033[31m{tx}%\033[m: {conta1+"0"}')
    print(f'Valor diminuido de \033[33m{moeda}{precovirgula}0\033[m com taxa de \033[34m{tx}%\033[m: {conta2+"0"}')

def metade(valor):
    contaM = valor / 2
    contaM = str(contaM).replace(".", ",")
    print(f'Metade: R$ {contaM}0')

def dobro(valor):
    contaD = valor * 2
    contaD = str(contaD).replace(".", ",")
    print(f'Dobro: R$ {contaD}0')



