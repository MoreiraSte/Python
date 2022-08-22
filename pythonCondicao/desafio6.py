num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1
menor = num1

if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
if (num2 < menor):
        menor = num2
if (num3 < menor):
        menor = num3

print(f'O maior é: {maior} O menor é: {menor}')

#usando lista:
# uva = []
 #for i in range(3):
  #   uva.append(int(input(f'Numero{i+1}:')))
#uva.sort()
#print(f'menor: {uva[0]} e maior: {uva[2]}')