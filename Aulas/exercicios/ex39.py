from datetime import date
ano = date.today().year
ano_informado = int(input('Informe o seu ano de nascimento: '))
idade = ano - ano_informado
if idade < 18:
    print(f'Você ainda não tem idade para se alistar, \033[31mainda faltam {18 - idade} anos!\033[m')
elif idade == 18:
    print(f'\033[32mEXÉRCITO BRASILEIRO\033[m\n\033[34mEstá na hora de se alistar!!!!\033[m')
elif idade > 18:
    print(f'\033[32mEXÉRCITO BRASILEIRO\033[m\n\033[31mJá passou {idade - 18} anos do seu alistamento!!\033[m')