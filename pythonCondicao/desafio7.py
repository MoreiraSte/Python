sal = float(input("Digite o seu salário: "))

if sal <= 1250:
    su = sal*0.15+sal

    print("Salario novo:", su)
else:
    su = sal * 0.10 + sal

print("Salario novo:",su)