import pandas as pd
import time
import numpy as np
import pyrebase


# classe
class Entidate:
    def __init__(self, nome='', numCnpj=0, razaoSocial='', email='', cep=0, sexo=''):
        self.nome = nome
        self.razaoSocial = razaoSocial
        self.email = email
        self.cep = cep
        self.sexo = sexo
        self.numCnpj = numCnpj

    def menu(self, nome='', numCnpj=0, razaoSocial='', email='', cep=0, sexo=''):

        global planilha
        while True:
            print("\n\n")
            print("\033[1;32m =-=" * 8 + "\033[0;0m")
            print("         BEM-VINDO AO MENU")
            print("\033[1;32m =-=" * 8 + "\033[0;0m")
            op = int(input("  \033[1;32m[1]\033[0;0m - Criar linha"
                           "\n  \033[1;32m[2]\033[0;0m - Consultar planilha"
                           "\n  \033[1;32m[3]\033[0;0m - Atualizar planilha"
                           "\n  \033[1;32m[4]\033[0;0m - Leitura da planilha"
                           "\n  \033[1;32m[5]\033[0;0m - Deletar elemento da planilha"
                           "\n  \033[1;32m[6]\033[0;0m - Finalizar"
                           "\n\n  \033[1;32mOPCÃO:\033[0;0m "))

            print("\033[1;32m =-=" * 8 + "\033[0;0m")

            # ADICIONAR
            if op == 1:

                print("\033[1;33m CARREGANDO.... \033[0;0m")
                time.sleep(6)

                planilha = pd.read_excel('EntidadeTemporaria.xlsx')

                linha = len(planilha) + 1

                for i in range(len(planilha.columns)):
                    planilha.loc[linha, planilha.columns[i]] = input(f'Insira {planilha.columns[i]}: ')
                    planilha.to_excel('EntidadeTemporaria.xlsx', index=False)

            # CONSULTAS
            if op == 2:

                print("\n\n")
                print("\033[1;94m =-=" * 10 + "\033[0;0m")
                print("              MENU CONSULTAR")
                print("\033[1;94m =-=" * 10 + "\033[0;0m")
                consultar = int(input("   \033[1;94m[1]\033[0;0m - Consultar profissão através da razão social"
                                      "\n   \033[1;94m[2]\033[0;0m - Consultar nome através do sexo"
                                      "\n   \033[1;94m[3]\033[0;0m - Consultar nome através do cnpj"
                                      "\n   \033[1;94m[4]\033[0;0m - Consultar bairro através do cep"
                                      "\n   \033[1;94mOPÇÃO:\033[0;0m "))
                print("\033[1;94m =-=" * 8 + "\033[0;0m")
                print("\n\n")

                if consultar == 1:
                    razaoSocial = input("Entre com a razao social: ")
                    print("\n\n")
                    print("\033[1;33m BUSCANDO DADOS... \033[0;0m")
                    time.sleep(10)
                    print("\n\n\n\n")
                    planilha = pd.read_excel('EntidadeTemporaria.xlsx')
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    print(planilha.loc[planilha['RazaoSocial'] == razaoSocial, ['ProfissaoRepresentanteLegal']])
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    time.sleep(8)

                if consultar == 2:
                    sexo = input("Sexo (use apenas M ou F):  ")
                    print("\n\n")
                    print("\033[1;33m BUSCANDO DADOS... \033[0;0m")
                    time.sleep(10)
                    print("\n\n\n\n")
                    planilha = pd.read_excel('EntidadeTemporaria.xlsx')
                    x = planilha.loc[planilha['SexoRepresentanteLegal'] == sexo, ['NomeRepresentanteLegal']]
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    print(x.to_string())
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    time.sleep(8)

                if consultar == 3:
                    numCnpj = float(input("Número cnpj: "))
                    print("\n\n")
                    print("\033[1;33m BUSCANDO DADOS... \033[0;0m")
                    time.sleep(10)
                    print("\n\n\n\n")
                    planilha = pd.read_excel('EntidadeTemporaria.xlsx')
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    print(planilha.loc[planilha['NumeroCNPJ'] == numCnpj, ['NomeRepresentanteLegal']])
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    time.sleep(8)

                if consultar == 4:
                    cep = float(input("cep: "))
                    print("\n\n")
                    print("\033[1;33m BUSCANDO DADOS... \033[0;0m")
                    time.sleep(10)
                    print("\n\n\n\n")
                    planilha = pd.read_excel('EntidadeTemporaria.xlsx')
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    print(planilha.loc[planilha['NumeroCEP'] == cep, ['NomeBairro']])
                    print("\033[1;94m =-=" * 10 + "\033[0;0m")
                    time.sleep(8)

            # ATUALIZAR/UPDATE
            if op == 3:

                print("Nos informe a coluna e a linha do elemento que deseja editar:")
                print("\n")
                upColu = input("Escolha coluna do elemento que deseja editar: ")
                print("\n")
                upLine = int(input("Informe o index da linha do elemento que deseja editar: "))
                print("\n")
                valor = input("Digite o novo valor: ")
                print("\n")
                planilha = pd.read_excel('EntidadeTemporaria.xlsx')

                print("\033[1;94m =-=" * 10 + "\033[0;0m")
                resp = int(input("SELECIONE O TIPO DE ELEMENTO:"
                                 "\n\033[1;94m[1]\033[0;0m - Texto"
                                 "\n\033[1;94m[2]\033[0;0m - Valor"
                                 "\n\033[1;94mOPCÃO:\033[0;0m"))

                print("\033[1;94m =-=" * 10 + "\033[0;0m")
                print("\n")

                if resp == 1:
                    planilha.at[upLine - 2, upColu] = valor.upper()

                if resp == 2:
                    valorFloat = float(valor)
                    planilha.at[upLine - 2, upColu] = valorFloat

                planilha.to_excel('EntidadeTemporaria.xlsx')
                print("\033[1;33m PLANILHA ATUALIZADA... \033[0;0m")
                time.sleep(8)

            # LEITURA/IMPRESSÃO
            if op == 4:
                print("\033[1;33m BUSCANDO DADOS... \033[0;0m")
                time.sleep(10)
                print("\n\n\n\n")
                mostrar = pd.read_excel("EntidadeTemporaria.xlsx")
                print("\033[1;92m=-=" * 300 + "\033[0;0m")
                print(mostrar.to_string())
                print("\033[1;92m=-=" * 300 + "\033[0;0m")
                time.sleep(8)

            # DELETE
            if op == 5:
                planilha = pd.read_excel("EntidadeTemporaria.xlsx")
                id = int(input("Entre com o id da linha que deseja excluir: "))
                planilha = planilha.drop(id - 2)
                planilha.to_excel("EntidadeTemporaria.xlsx", index=False)
                time.sleep(8)


            # Sair
            if op == 6:
                print("\033[1;91m Finalizando..... \033[0;0m")
                time.sleep(7)
                break


