lados=[]
perimetro=0
for i in range(3):
    lado = float(input(f"Insira o {i+1}º lado: "))
    lados.append(lado)
for lado in lados:
    perimetro+=lado
print("Perimetro igual:",perimetro)