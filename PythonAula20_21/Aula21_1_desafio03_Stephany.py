from random import sample
print("Sorteados:")
print('-'*10)
num = tuple(sample(range(10), 5))

for i in num:
    print(i, end=' ')

print("\n")
print('-'*10)

print(f'''
Maior valor sorteado: {max(num)}
Menor valor sorteado: {min(num)}.''')

print('-'*30)