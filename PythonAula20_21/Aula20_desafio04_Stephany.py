
n = int(input("Digite um numero: "))

for i in range(n+1):

    if n % (i+1) == 0:
        print("\33[31m",i, end=" " "\33[m")

    else:
        print("\33[34m",i, end=" " "\33[m")

if (n%2) == 1:
    print(end="\n" f'O numero {n} é primo')

else :
    print(end="\n" f'O numero {n} não é primo')


