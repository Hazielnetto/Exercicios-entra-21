numeros=[]
for i in range(2):
    numero=int(input(f"Digite o {i+1}º numero: "))
    numeros.append(numero)
print("Quociente é:",(numeros[0] / numeros[1]))
print("Resto é:",numeros[0]%numeros[1])