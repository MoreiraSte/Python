from math import sqrt

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacete: "))

h = (oposto**2) + (adjacente**2)
raiz = sqrt(h)

print(raiz)