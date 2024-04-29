def gravar (path, nomes):
    arquivo = open(path, 'w')
    for n in nomes:
        arquivo.write(n)
        arquivo.write("\n")
    arquivo.close()