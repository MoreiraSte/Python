import pandas as pd

planilha = pd.read_excel("pessoas.xlsx")

qde = planilha['Nome'].count()

id = int(input('Digite id: '))
nome = input('Digite o nome: ')
idade = int(input('digite a idade: '))
peso = float(input('Digite o peso: '))

#d = {'Id':[id], ['Nome'] : [nome], ['idade']:[idade],['peso']: [peso]}


planilha.loc[qde+1 , 'ID'] = id
planilha.loc[qde+1 , 'Nome'] = nome
planilha.loc[qde+1 , 'Idade'] = idade
planilha.loc[qde+1 , 'Peso'] = peso


planilha.to_excel('pessoas.xlsx', index=False)


