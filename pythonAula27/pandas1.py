#mais usada
# trata planilha apenas como base de dados
# faz o que quiser com o arquivo, flexível
# openpyxl -> trata planilha como planilhas, edits como se fosse VBA
# menos eficiente, mantém as fórmulas

import pandas as pd
#import matplotlib as mt

planilha = pd.read_excel("pessoas.xlsx")


qde_linhas =  planilha['Nome'].count()
for i in range(qde_linhas):
    if planilha['Nome'][i] == 'ABRAAO SILVA DE LIMA':
        print([i])





# faz contagem das linhas da coluna nome e percorrendo na contagem, imprime sem o index
# qde_linhas =  planilha['Nome'].count()
# for i in range(qde_linhas):
#     print(planilha['Nome'][i])

# qde_linhas =  planilha['Nome'].count() # faz a contagem de linhas, quantos elementos tem na coluna nome nesse caso
# print(qde_linhas)
#print(planilha['Nome'][2]) # com o nome e o indice, podemos buscar um nome especifico
# for dado in planilha:
#     print (dado) # imprime os titulos das colunas, no caso é : id,nome,idade e peso
