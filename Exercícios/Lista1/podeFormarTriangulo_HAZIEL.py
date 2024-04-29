triangulo=[]
for i in range(3):
    reta = float(input(f"Digite o valor do {i+1}º segmento de reta: "))
    triangulo.append(reta)
if ((triangulo[0] + triangulo[1]) > triangulo[2] and (triangulo[0] + triangulo[2]) > triangulo[1] and (triangulo[1] + triangulo[2]) > triangulo[0]):
    print("Pode formar um triângulo")    
else:
    print("Não pode formar um triângulo")

