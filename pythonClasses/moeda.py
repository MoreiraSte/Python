class moeda:
    def __init__(self,valor,tx,preco,formato):
        self.valor = valor
        self.tx = tx
        self.preco = preco
        self.formato = formato

    def aumentar(self, preco,tx,formato=False):
        conta = preco + tx
        return conta if not formato else moeda(conta)

    def diminuir(self, preco,tx,formato=False):
        conta2 = preco - tx
        return conta2 if not formato else moeda(conta2)



    def metade(self, preco,tx, formato=False):
        conta3 = preco / tx

        return conta3 if not formato else moeda(conta3)

    def dobro(self, preco,tx, formato=False):
        conta4 = preco * tx


        return conta4 if not formato else moeda(conta4)

    def moeda(self, preco,moeda ='R$'):
        return f'{moeda}{preco:>.2f}'.replace('.', ',')
