resposta = input("Deseja iniciar? S ou N\n")
while (resposta == 's' or resposta == 'S'):
    numero = int(input("Digite o número: "))
    if numero%3 == 0 and numero%5 == 0:
        print("FizzBuzz")
    elif numero%3 == 0:
        print("Fizz")
    elif numero%5 == 0:
        print("Buzz")    
    else:
        print(numero)