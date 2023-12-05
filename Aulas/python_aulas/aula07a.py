# nome=input('Qual é seu nome? ')
# print('Prazer em te conhecer{:=^20}!'.format(nome))
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}, a multiplicação vale {m}, a divisão vale {d:.3f}', end=' ')
print(f'Divisão inteira vale {di}, e potência vale {e}.')