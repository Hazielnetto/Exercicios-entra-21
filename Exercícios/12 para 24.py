def converterHora(horas, minutos):
    if horas > 12:
        horas = horas - 12
        ampm="pm"
    elif horas == 12:
        ampm="pm"
    else:
        ampm='am'
    return str(horas) + ':' + str(minutos) + ' ' + ampm

def inverteNome(nome):
    li = list(nome)
    li.reverse()
    return ''.join(li).upper()

print(inverteNome('Edilson'))