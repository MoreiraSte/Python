def escreva(texto):

    tamanho = len(texto) + 4
    print("~" * tamanho)    
    print(f"  {texto}")
    print("~" * tamanho)    

if __name__=='__main__':
    for i in range (0,3):
        texto= str(input("Digite a mensagem: "))
        escreva(texto)