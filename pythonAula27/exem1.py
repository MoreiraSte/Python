#var = input('Digite um valor: ')

try:
    file = open('texto.txt','w',encoding='utf8')
    file = file.read()
    file = file.split('\n')
    for linha in range(len(file)):
            print(file[linha])
finally:
    file.close()
#print(file)
# file.write('Linha1\n')
# file.write('Linha2\n')
#file.write(f'{var}\n')
# file.close()
