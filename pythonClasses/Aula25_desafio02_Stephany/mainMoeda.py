from moeda import *

preco = float(input('preco em R$: '))
tx = float(input('Taxa: '))
# f2 = aumentar(valor,"R$", tx)
# f3 = diminuir(valor,"R$", tx)

f6 = moeda(preco,"R$",tx)
f4 = metade(preco)
f5 = dobro(preco)
