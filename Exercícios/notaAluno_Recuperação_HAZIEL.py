media= 0 
cont=0  
alunos=int(input("Quantos alunos: "))
for x in range(alunos):   
  media = int(input("Média: ")) 
  if(media >= 3 and media <= 5):
   cont= cont + 1
  while media>10 or media<0:
   media=float(input("Nota invalida, digite uma nota entre 0 e 10: "))
print(cont," Aluno(s) ficaram de RECUPERAÇÃO")