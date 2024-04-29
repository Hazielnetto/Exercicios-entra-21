from random import randint
numero=randint(1,10)
chute=int(input("Chute um número de 1 a 10: "))
while numero != chute:
    chute=int(input("Tente novamente: "))
print("Parabéns, você acertou!")