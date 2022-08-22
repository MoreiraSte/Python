from pessoas import *
from arquivo import *

arq = 'pessoas.txt'

if not arqExist(arq):
    create(arq)


while True:
    resp = menu(["1 - Novo Cadastro", "2 - Pessoas Cadastradas", "0 - Sair"])

    if resp == 1:
       cabecalho('NOVO CADASTRO')
       nome = input('Nome: ')
       idade = int(input("Idade:  "))
       cadastrar(arq,nome,idade)
    elif resp == 2:
        lerArq(arq)
    elif resp == 3:
        print("Saindo do sistema....")
        break
    else:
        print("Erro! Digite uma das tres opções")