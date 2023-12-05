from datetime import date
ano_vetor = []
ano_atual = date.today().year
a=1
for i in range(1,8):
    ano_nascimento = int(input(f'Informe o {i}ª ano de nascimento: '))
    ano_vetor.append(ano_nascimento)
for ano in ano_vetor:
    idade = ano_atual - ano
    if idade > 18:
        frase = '\033[33mATINGIU A MAIORIDADE\033[m'
    elif idade == 18:
        frase = '\033[33mATINGIU A MAIORIDADE ESSE ANO\033[m'
    else:
        frase = '\033[33mNÃO ATINGIU A MAIORIDADE\033[m'
    print(f'A {a}ª pessoa nasceu em {ano} e tem {idade} anos e {frase}!')
    a+=1