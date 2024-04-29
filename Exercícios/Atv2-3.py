def tirapont(texto):
    
    pontuacao = ['.', ',', '?', '!', ';', ':','"',"'",'(',')','[',']','{','}h']

    for i in pontuacao:
        texto = texto.replace(i, '')

    return texto

palavra = {}

texto1 = str(input('Digite o texto: '))
texto1 = tirapont(texto1).split()

for i in texto1:

    if i in palavra.keys():
        palavra[i] += 1

    else:
        palavra[i] = 1

for chave, valor in palavra.items():
    print(chave, valor)