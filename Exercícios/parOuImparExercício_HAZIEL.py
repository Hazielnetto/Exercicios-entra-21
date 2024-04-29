resposta = input("Deseja Iniciar? S ou N\n")
while (resposta == "s" or resposta == "S"):
 numero = int(input("Digite o número: "))
 if numero%2 > 0:
    print(" IMPAR\n")
 else:
    print (" PAR\n")