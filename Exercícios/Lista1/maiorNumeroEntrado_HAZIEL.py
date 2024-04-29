numeros=[]
for i in range(2):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
if numeros[0] > numeros[1]:
    print("Maior número entrado:",numeros[0])
else:
    print("Maior número entrado:",numeros[1])