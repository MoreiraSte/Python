from pessoas import *

def arqExist(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError :
        return False
    else:
        return True

def create(nome):
    try:
        a =open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação")
    else:
        print(f'{nome} Criado com sucesso')

def lerArq(nome):
    try:
        a =open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')

    finally:
      a.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a= open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:

            a.write(f'{nome}{idade}\n')
        except:
            print('Houve um erro na hora de ler os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()