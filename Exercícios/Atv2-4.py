def palin(texto):
    
    if texto == texto[::-1]:

        return 'É um palíndromo!'
    else:

        return 'Não é um palíndromo!'

texto1 = str(input('Digite o texto: '))
print(palin(texto1))