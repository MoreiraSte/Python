listnum = []
cont = 0
while True:
    listnum.append(int(input("Digite um valor:  ")))
    cont +=1
    resp = str(input("Deseja continuar? [S/N]: "))
    if resp in 'Nn':
           break

print(f'Quantidade de valores: {cont}')
listnum.sort(reverse=True)
print(f'Valores decrescentes: {listnum}')
if 5 in listnum:

 print("O numero 5 esta na lista")

else:
  print("O numero 5 não esta na lista")