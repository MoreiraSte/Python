def area(largura,comprimento):

    a = largura * comprimento
    print(f'A area total: {a}m²')


if __name__=='__main__':
    area(float(input("Largura: ")),float(input("Comprimento: ")))
