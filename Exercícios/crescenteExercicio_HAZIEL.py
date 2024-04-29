numero=[]
numeros=[]
for x in range(3):   
    numero = int(input(f"Digite o número {x+1}: ")) 
    numeros.append(numero)
if numeros[0] < numeros[1]:
    if numeros[1] < numeros[2]:
        print("Crescente")
else:
  print("Não está em ordem crescente")