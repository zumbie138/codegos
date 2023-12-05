casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
ano = int(input('Digite quantos anos vai levar para pagar: '))
prestacao = casa / (ano*12)
if prestacao > salario*0.30:
    print(f'A prestação é de R${prestacao:.2f}, e 30% do salário é R${salario*0.30:.2f}\nPortanto o empréstimo \033[31mNÃO FOI\033[m aprovado.')
else:
    print(f'A prestação é de R${prestacao:.2f}, e 30% do salário é R${salario*0.30:.2f}\nPortanto o empréstimo \033[32mFOI\033[m aprovado!')