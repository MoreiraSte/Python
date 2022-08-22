def calculo():
    soma = 0
    mult =0
    novos = 0
    max = 0

    n = int(input("Digite o 1° numero: "))
    n2 = int(input("Digite o 2° numero: "))

    opcao = int(input("[1] - somar "
                      "[2] - multiplicar"
                      "[3] - maior"
                      "[4] - novos numeros"
                      "[5] - sair do programa"))

    while opcao > 0:

        if opcao == 1:
            soma = n + n2
            print("Soma: {}".format(soma))

            break


        elif opcao == 2:
            mult = n*n2
            print("Multiplicação: {}".format(mult))
            break

        elif opcao == 3:
            if n > max:
                max = n
            if n2 > max:
                max = n2

            print("O maior numero é: {}".format(max))
            break

        elif opcao == 4:
            n3 = int(input("Digite o novo 1° numero: "))
            n4 = int(input("Digite o novo 2° numero: "))

            n = n3
            n2 = n4
            break

        elif opcao == 5:
            break

calculo()