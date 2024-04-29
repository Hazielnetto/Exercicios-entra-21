char = {}
texto = str(input('Digite o texto ou palavra: '))

for i in texto:

    if i not in char.keys():
        char[i] = 1

print(f'{len(char)}')