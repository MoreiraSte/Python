try:
    with open('texto.txt','w+',encoding='utf8') as file:
        file.write('Vini\n')
        file.write('Pedro\n')
        file.seek(0)
        print(file)
finally:
    file.close()
