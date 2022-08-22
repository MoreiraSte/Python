from datetime import date

bis = int(input("digite o ano desejado ou '0' para o atual: "))


if bis == 0:
    bis = date.today().year
    print(f'Estamos em {bis}')

if (bis%4==0 and bis%100!=0) or (bis%400==0):
    print("O ano", bis, "é bissexto")
else:
    print("O ano", bis, "não é bissexto")

