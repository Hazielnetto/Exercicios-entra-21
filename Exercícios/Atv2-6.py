def escreveExtenso(num):

    if num > 999 or num < 0:

        return('Número inválido')

    num = str(num)

    if len(num) == 3 and num[0] == '0':

        if num[1] == '0':            
            num = num[2]

        else:
            num = num[1:]

    elif len(num) == 2 and num[0] == '0':
        num = num[1]

    num_ext = ''

    if int(num) == 100:

        return 'Cem'

    elif int(num) == 10:

        return 'Dez'

    elif int(num) == 0:

        return 'Zero'

    centena = {'9': 'Novecentos', '8': 'Oitocentos', '7': 'Setecentos', '6': 'Seiscentos', '5': 'Quinhentos', '4': 'Quatrocentos', '3': 'Trezentos', '2': 'Duzentos', '1': 'Cento'}

    dezena = {'9': 'Noventa', '8': 'Oitenta', '7': 'Setenta', '6': 'Sessenta', '5': 'Cinquenta', '4': 'Quarenta', '3': 'Trinta', '2': 'Vinte'}

    dezeuni = {'19': 'Dezenove', '18': 'Dezoito', '17': 'Dezessete', '16': 'Dezesseis', '15': 'Quinze', '14': 'Quatorze', '13': 'Treze', '12': 'Doze', '11': 'Onze', '10': 'Dez'}

    unidade = {'9': 'Nove', '8': 'Oito', '7': 'Sete', '6': 'Seis', '5': 'Cinco', '4': 'Quatro', '3': 'Três', '2': 'Dois', '1': 'Um'}

    if len(num) == 3:
        num_ext += centena[num[0]]

        if num[1] == '1':
            num_ext += ' e ' + dezeuni[num[1:]]

        elif num[1] == '0':
            if num[2] == '0':

                pass

            else:
                num_ext += ' e ' + unidade[num[2]]

        else:

            if num[2] == '0':
                num_ext += ' e ' + dezena[num[1]]

            else:
                num_ext += ' e ' + dezena[num[1]] + ' e ' + unidade[num[2]]

    elif len(num) == 2:
        if num[0] == '1':
            num_ext = dezeuni[num]

        else:
            num_ext += dezena[num[0]] + ' e ' + unidade[num[1]]

    else:
        num_ext += unidade[num]

    return num_ext

n = int(input('Digite um número (0 a 999): '))
print(f'{n} = {escreveExtenso(n)}')