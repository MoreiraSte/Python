expressao = str(input("Digite a expressão: "))
ex = []

for i in expressao:
    if i == '(':
        ex.append('(')
    elif i == ')':
        if len(ex) > 0:
            ex.pop()
        else:
            ex.append(')')
            break
if len(ex) == 0:
    print("Sua expressão é valida!")
else:
    print("Sua expressão é invalida!")