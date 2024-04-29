def maior_nome(nomes):
    nomes.sort(key=len, reverse=True)
    print(nomes[0])