peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe seu altura em metros: "))
imc=(peso//(altura**2))
if imc < 20:
    print(f"{imc} - Abaixo do normal")
elif imc >= 20 and imc < 25:
    print(f"{imc} - Normal")
elif imc >= 25 and imc < 30:
    print(f"{imc} - Sobrepeso")
elif imc >= 30 and imc < 35:
    print(f"{imc} - Obesidade Leve (I)")
elif imc >= 35 and imc < 40:
    print(f"{imc} - Obesidade Moderada (II)")
else:
    print(f"{imc} - Obesidade Mórbida (III)")