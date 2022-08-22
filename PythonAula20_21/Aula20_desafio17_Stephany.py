num = int(input('Digite um numero: '))
maior = num
menor = num
media = 0
soma=0

cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

while cc not in 'N':
    num = int(input('Digite um numero: '))

    soma +=num
    media = soma/4

    if num > maior:
        maior = num
    if maior < menor:
        menor = num

    cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

print('O MEDIA do número digitado foi {}.'.format(media))
print('O MAIOR número digitado foi {}.'.format(maior))
print('O MENOR número digitado foi {}.'.format(menor))