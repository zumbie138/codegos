salario = float(input('Informe seu salário: '))
if salario > 1250.0:
    aumento = salario*1.1
else:
    aumento = salario*1.15
print(f'Um salario de: R${salario:.2f}\nTêm um aumento para: R${aumento:.2f}')