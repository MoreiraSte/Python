lista =[]
cadastro =[]
cont = 0
maior = 0
menor = 99999999
while True:
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))

    cont += 1
    lista.append(nome)
    lista.append(peso)
    cadastro.append(lista[:])
    lista.clear()

    resp = str(input("Deseja contiuar? [S/N]: "))
    
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

    if resp.lower() == 'n':
        break
print(f'Dados cadastrados: {cadastro}')
print(f'Total de cadastros: {cont}')
print(f'Maior peso: {maior}Kg')
print(f'Menor peso: {menor}Kg')






