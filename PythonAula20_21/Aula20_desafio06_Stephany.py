ma=0
me=0
for i in range(1,8):
    ano = int(input("Digite o ano de nascimento da {}° pessoa: ".format(i)))

    if 2022 - ano >= 18:
        ma += 1

    else :
        me +=1

print(f'Total maiores: \33[34m{ma}\33[m')
print(end="\n")
print(f'Total menores: \033[31m{me}\33[m')
