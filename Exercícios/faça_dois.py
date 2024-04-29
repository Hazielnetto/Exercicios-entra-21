'''2  - Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, faça_dois é uma 
função que toma um objeto de função como argumento e o chama duas vezes:
def faça_dois (f):
    f()
    f()
Aqui está um exemplo que usa faça_dois para chamar uma função chamada print_spam duas vezes:
def print_spam():
    print('spam')
do_twice(print_spam)
Digite este exemplo em um script e teste-o.
Altere faça_dois  para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como 
um argumento.
Copie a definição de printa_dois que aparece anteriormente neste capítulo no seu script.
Use a versão alterada de printa_dois para chamar printa_dois duas vezes, passando 'spam' como um argumento.
Defina uma função nova chamada repita_quatro que receba um objeto de função e um valor e chame a função quatro vezes, 
passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.
Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros recursos que aprendemos até agora.
'''
def minha_mae(mae):
    print(mae)


def faca_dois(f,cu):
    f(cu)
    f(cu)
    
faca_dois(minha_mae,'cu')
