from random import randint
resposta=input("Deseja Iniciar o programa? S ou N: ")
while resposta.upper() == 'S':
    print(randint(1,6),"\n")
    resposta=input("Repetir? S ou N: ")
    if resposta.upper() != 'S':
        break
