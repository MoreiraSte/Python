texto= 'Tecnico de Desenvolvimento de Sistemas'

#print(texto.upper())

#--------------------
for i in texto:
   print(i, end='')

print('     FIM')
#---------------------
for i in range(10):
    print(texto[i])

print('     FIM')
#---------------------
print(f'{len(texto)}')
for i in range(len(texto)):
    print(texto[i], end='')
#---------------------
texto ='Senai'
for i in range(len(texto)):
    print(texto[::-1].upper())
#-----------------------------
for i in range(len(texto)):
    print(texto[i].upper())









