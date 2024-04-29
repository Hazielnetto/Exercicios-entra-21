numero=input("Digite um número: ")
while numero != '0':    
    aux=0
    for i in range(len(numero)):
        inteiro = int(numero[i])
        inteiro = inteiro**(len(numero))
        aux+=inteiro
        print(inteiro)
    print(aux)
    if aux == int(numero):
        print("Esse número FAZ parte dos Números de Armstrong")
    else:
        print("Esse número NÃO faz parte dos Números de Armstrong")
    numero=input("Digite outro número: ")