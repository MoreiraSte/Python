reta = int(input("Digite a 1° reta: "))
reta2 = int(input("Digite a 2° reta: "))
reta3 = int(input("Digite a 3° reta: "))

if reta < (reta2+reta3) and reta2 < (reta+reta3) and reta3 < (reta2+reta):
    print("Podem formar triangulos")

else:
    print("Nao podem formar triangulos")