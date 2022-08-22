tel = input("Digite o telefone: ")

if(len(tel) <= 8 ):
    print(f'Numero corrigido: 9{tel}')

else:
    print(f'Seu numero de telefone: {tel}')