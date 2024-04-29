def filtro(nomes,c):
    n = list(filter(lambda x: x[0].lower() == c, nomes))
    return n