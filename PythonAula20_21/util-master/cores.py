# Esta biblioteca serve para você não precisar ficar se preocupando com as cores
# e com digitar \33['blabla'm

# Biblioteca com todas cores em dicionários
# feita por eu viktor podem usar e ser feliz
# para usar com eficácia siga o modelo de print a seguir:
# print("{}{}{} SEU TEXTO {}".format(cores['cor_da_letra'], bg['cor_do_fundo'],
# fx['efeito_do_texto'], limpar))
# O limpar no final é necessário para remover os efeitos no final da linha, para que
# ele não siga para o resto do texto

limpar = '\33[m'

cores = {
    'preto': '\33[30m',
    'vermelho': '\33[31m',
    'verde': '\33[32m',
    'amarelo': '\33[33m',
    'azul': '\33[34m',
    'roxo': '\33[35m',
    'ciano': '\33[36m',
    'cinza': '\33[37m',

    'cinza_escuro': '\33[90m',
    'vermelho_claro': '\33[91m',
    'verde_claro': '\33[92m',
    'amarelo_claro': '\33[93m',
    'azul_claro': '\33[94m',
    'roxo_claro': '\33[95m',
    'ciano_claro': '\33[96m',
    'branco': '\33[97m'
}

bg = {
    'branco': '\33[107m',
    'preto': '\33[40m',
    'vermelho': '\33[101m',
    'verde': '\33[102m',
    'amarelo': '\33[103m',
    'azul': '\33[104m',
    'roxo': '\33[105m',
    'ciano': '\33[106m',
}

fx = {
    'normal': '\33[10m',
    'contorno': '\33[52m',
    'negrito': '\33[1m',
    'italico': '\33[3m',
    'sublinhado': '\33[4m',
}
