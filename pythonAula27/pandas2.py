import pandas as pd

dados = {'ID': [1, 2, 3], 'Nome': ['Bruna', 'Sophia', 'Maria'], 'Idade': [20, 25, 29], 'Altura': [1.70, 1.68, 1.79]}

dataF = pd.DataFrame(data=dados)

dataF.to_excel('exemplo.xlsx', index =False )

planilha = pd.read_excel('exemplo.xlsx')
print(planilha)

#data frame -> planilha virtual
