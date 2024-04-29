def mesExtenso(mes):
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho', 'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    return meses[mes-1]

data = input("Digita sua data de nascimento (dd/mm/aaaa): ")
dia = data[0:2]
mes = int(data[3:5])
ano = data[6:10]

print('\nSua data de nascimento: ', dia,'de', mesExtenso(mes),'de', ano,'\n')

