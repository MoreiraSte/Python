def maior(num):


    maior = num
    menor = num
    list = []
    list.append(num)
    cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

    while cc not in 'N':
        num = int(input('Digite um numero: '))
        list.append(num)

        if num > maior:
            maior = num
        if maior < menor:
            menor = num

        cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

    print('-'*30)

    print('Analisando os valores')
    print(list)
    print('O MAIOR VALOR: {}.'.format(maior))
    print('-'*30)



if __name__=='__main__':

    maior(int(input('Digite um numero: ')))