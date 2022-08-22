string = input("Digite uma palavra ou frase qualquer: ")
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print("O texto digitado" "\33[34m é palindromo \33[m")
else:
    print("O texto digitado" "\33[31m não é palindromo \33[m")