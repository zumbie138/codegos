n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
print('APROVADO' if m >=6 else 'REPROVADO')
# if m >= 6.0:
#     print('Sua média foi boa! APROVADO!')
# else:
#     print('Sua média foi ruim! REPROVADO!')