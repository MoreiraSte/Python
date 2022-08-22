num = 0
soma = 0
cont = 0

while True:

    num = int(input("Digite um numero [999 para parar]: "))
    cont += 1

    if num == 999:
        break
    soma += num


print(f'A soma dos {cont} numeros foi: {soma}')