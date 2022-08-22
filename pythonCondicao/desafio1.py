from random import randint

num = int(input("Pense em um número de 1 a 5 e digite: "))
var= randint(1,5)
if num == var:
    print("Você acertou, eu pensei em",var,"e vc digitou",num)

else:
    print(f'Você perdeu, pois eu pensei em {var} e voce em {num}')