listanum = []

for y in range(0,5):
    n = int((input(f'Digite o {y}° numero: ')))

    if y == 0 or n > listanum[-1]:
        listanum.append(n)
    else:
        ordem = 0
        while ordem < len(listanum):
            if n <= listanum[ordem]:
                listanum.insert(ordem,n)
                break
            ordem +=1
print(listanum)
