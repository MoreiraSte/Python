numero = int(input("Digite um numero de 1000 a 9999: "))

u = numero // 1 % 10
d = numero // 2 % 10 - u
c = numero // 2 % 9 - d
m = numero // 3 % 10
print(f'Unidade: {u} Dezena: {d} Centena: {c} Milhar: {m}')

num = str(numero)
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')





