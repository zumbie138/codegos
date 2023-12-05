from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Coloque seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(f'O atleta tem \033[33m{idade}\033[m anos e é da categoria \033[1;34mMIRIM\033[m.')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem \033[33m{idade}\033[m anos e é da categoria \033[1;34mINFANTIL\033[m.')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem \033[33m{idade}\033[m anos e é da categoria \033[1;34mJUNIOR\033[m.')
elif idade > 19 and idade <=20:
    print(f'O atleta tem \033[33m{idade}\033[m anos e é da categoria \033[1;34mSÊNIOR\033[m.')
elif idade >20:
    print(f'O atleta tem \033[33m{idade}\033[m anos e é da categoria \033[1;34mMASTER\033[m.')
        