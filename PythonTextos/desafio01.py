texto = input("Digite seu nome: ")

print(f'letras maiusculas: {texto.upper()}')
"\ln"
print(f'letras minusculas: {texto.lower()}')
"\ln"
print(f'quantas letras com espaços: {(len(texto))}')
"\ln"
print(f'quantas letras sem espaços: {len("".join(texto.split()))}')
"\ln"
texto2 = texto.split()
print(f'quantas letras tem o primeiro nome: {len(texto2[0])}')