n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a primeira nota"))

media = (n1+n2)/2

if(media <= 3):
    print(f'nota={media}, portanto voce esta Reprovado')

elif media < 5:
    print(f'nota={media}, portanto esta de Recuperação')

elif media <7:
    print(f'nota={media}, portanto sua nota é Regular')

else:
    print(f'nota={media}, portanto voce esta aprovado')

