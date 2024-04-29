def procuraValor(dicio, valor):
    
    chaves = []

    for chave, val in dicio.items():

        if val == valor:
            chaves.append(chave)

    return chaves

dicionario={'haziel':'18', 'lucas':'18', 'maria':'19', 'eduardo':'19', 'jorge':'18'}
v = str(input('Valor a ser procurado: '))

print(procuraValor(dicionario, v))