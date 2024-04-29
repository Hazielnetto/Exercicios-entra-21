import leitura
import manipula
import impressao

nomes = leitura.lerArquivo('nomes.txt')
nome_filtro = manipula.filtro(nomes, 'a')
impressao.maior_nome(nome_filtro)

print(nome_filtro)