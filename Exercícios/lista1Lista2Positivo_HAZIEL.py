lista1 = [123,43,45,46,76,87,69,3,-13,-14,-15,-16]
lista2 = []
for x in range(len(lista1)):
    if lista1[x] >=0:
        lista2 = lista1
print(*lista2)