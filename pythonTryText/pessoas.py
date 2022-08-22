def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except (ValueError,TypeError):
            print('Erro! Digite um numero inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('Usuario preferiu nao digitar esse numero')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for item in lista:
        print(f'{item}')

    print(linha())
    op = leiaInt('Opção: ')
    return op