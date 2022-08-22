x = 0
for i in range(1,7):
    n = int(input("Digite o {}° numero: ".format(i)))
    if n % 2 == 0:
        x += n

print(f'O resultado total é: {x}')

