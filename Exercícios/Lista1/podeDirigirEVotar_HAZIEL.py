idade=int(input("Digite a idade: "))
if idade >= 16 and idade < 18:
    print("Pode votar mas não pode dirigir!")
elif idade >= 18:
    print("Pode dirigir e pode votar!")
else:
    print("Não pode dirigir nem votar!")