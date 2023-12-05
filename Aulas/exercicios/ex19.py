from random import randint
aluno1 = input('coloque o nome do primeiro aluno: ')
aluno2 = input('coloque o nome do segundo aluno: ')
aluno3 = input('coloque o nome do terceiro aluno: ')
aluno4 = input('coloque o nome do quarto aluno: ')
relacao = {'1':aluno1,'2':aluno2,'3':aluno3,'4':aluno4}
sorteio = str(randint(1,4))
print(f'O aluno sorteado foi o: {relacao[sorteio]}')