from random import randint
vetor_aux=[]
ordem=1
aluno1 = input('coloque o nome do primeiro aluno: ')
aluno2 = input('coloque o nome do segundo aluno: ')
aluno3 = input('coloque o nome do terceiro aluno: ')
aluno4 = input('coloque o nome do quarto aluno: ')
relacao = [aluno1,aluno2,aluno3,aluno4]
while True:
    if len(vetor_aux) == 4:
        break
    indice = randint(0,3)
    if indice in vetor_aux:
        continue
    else:
        print(f'{ordem}º aluno: {relacao[indice]}')
        vetor_aux.append(indice)
        ordem+=1
