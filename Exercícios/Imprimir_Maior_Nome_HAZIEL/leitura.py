def lerArquivo(path):
    arquivo = open(path, 'r')
    nomes=[]
    for linha in arquivo:
        nomes.append(linha.strip())
    arquivo.close()
    return nomes