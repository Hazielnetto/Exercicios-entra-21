numeros=[]
for i in range(3):
    numero=int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
for j in range(3):
    mem='n'
    print(numeros)
    for c in range(len(numeros)-1):
        if numeros[c] > numeros[c+1]:
            mem=numeros[c]
            numeros[c] = numeros[c+1]
            numeros[c+1]=mem
    if mem == 'n':
                break