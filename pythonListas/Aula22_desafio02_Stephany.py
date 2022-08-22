dados = [0]
count = 0
while True:
    n = int(input("Digite valor: "))

    for i in dados:
        if n == i:
            count+=1

    if count <= 0:
        dados.append(n)
        print(dados)
        resp = input("Deseja continuar ? [S/N]")

        if resp.upper() == 'S':
            continue

        elif resp.upper() == 'N':
            dados.remove(0)
            print(f'Lista: {dados}')
            break
    else:
        print("Valor duplicado, insira novamente")
        count = 0


