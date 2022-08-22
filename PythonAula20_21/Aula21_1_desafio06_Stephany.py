palavras = ('CAROLINE','DANYELLY','GABY','GEOVANA','LIMA',
            'SANTOS','ISABELLA','JAMILE','JULIA','LEONARDO',
            'LUIZ','MILENA','NATHAN','NICOLLY','RYAN','CABRAL','VINICIUS')

for p in palavras:
    print(f'\nNa palavra {p} temos:  ',end=' ')

    for letra in p:
        if letra.lower() in 'aeiou':
            print('\33[31m',letra,'\33[m', end=' ')