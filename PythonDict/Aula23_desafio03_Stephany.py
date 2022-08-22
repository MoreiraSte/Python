from datetime import datetime

documents = dict()


documents['nome'] = input("Nome: ")
anoNasc = int(input("Ano de nascimento: "))
documents['idade'] = datetime.now().year - anoNasc
documents['ctps'] = int(input("Carteira de trabalho: "))

if documents['ctps'] != 0 :

    documents['anoCont'] = int(input("Ano de contratação: "))
    documents['sal'] = float(input("Salário: "))
    documents['aposentadoria'] = documents['idade'] + ((documents['anoCont'] + 35) - datetime.now().year)


for i, x in documents.items():
    print(f' - {i} = {x}')