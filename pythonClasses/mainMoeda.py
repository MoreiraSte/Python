from moeda import *

preco = float(input('preco em R$: '))
tx = float(input('Taxa: '))


print(f'A metade de {moeda.moeda(self= moeda,preco)} é {moeda.metade(preco,tx, True)}')
# print(f'Valor aumentado de {moeda.moeda(preco)}\33[33mR${preco:.2f}\33[m com taxa de \33[31m{tx:.0f}%\33[m : {moeda.aumentar(preco,tx,True)}')
# print(f'Valor diminuindo de \33[33mR${preco:.2f}\33[m com taxa de \33[31m{tx:.0f}%\33[m : {moeda.diminuir(preco,tx,True)}')
# print(f'Metade:{moeda.metade(preco,tx,True)}')
# print(f'Dobro: {moeda.dobro(preco,tx,True)}')



