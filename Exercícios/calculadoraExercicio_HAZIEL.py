resposta = input("Deseja Iniciar? S ou N\n")
while resposta.upper() == 'S':
    operacao = int(input("Qual operação?\n1 - soma\n2 - subtração\n3 - divisão\n4 - multiplicação\n5 - sair\n"))
    if operacao > 0 and operacao < 6:  
        numero = []
        numeros = []      
        if operacao == 1:
            operacao_print = '+'
            for x in range(0,2):
                numero = int(input())
                numeros.append(numero)
                print(operacao_print)
                operacao_print='='
            print(numeros[0] + numeros[1])

        if operacao == 2:
            operacao_print = '-'
            for x in range(2):
                numero = int(input())
                numeros.append(numero)
                print(operacao_print)
                operacao_print='='
            print(numeros[0] - numeros[1])

        if operacao == 3:
            operacao_print = '/'
            for x in range(2):
                numero = int(input())
                numeros.append(numero)
                print(operacao_print)
                operacao_print='='
            print(numeros[0] / numeros[1])

        if operacao == 4:
            operacao_print = '*'
            for x in range(2):
                numero = int(input())
                numeros.append(numero)
                print(operacao_print)
                operacao_print='='
            print(numeros[0] * numeros[1])

        if operacao == 5:
            print("Até a próxima")
            break
    else:
        print("Número inválido, digite um número entre 1 e 5")