primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
quantidade = 10
total = 0

while True:
    numeros = range(primeiro_termo, primeiro_termo + quantidade * razao, razao)
    total += len(numeros)
    print(*numeros, sep=' ', end=' ')
    quantidade = int(input('\nQuantos termos a mais você quer mostrar?: \n'))
    if quantidade == 0:
        break


    primeiro_termo = numeros[-1] + razao

print("Fim.")