n=input('Digite qualquer coisa para saber seu tipo primitivo: ')
if n.isnumeric():
    a='é'
else:
    a='não é'
if n.isdecimal():
    b='é'
else:
    b='não é'
if n.isalpha():
    c='é'
else:
    c='não é'
print(f'Oque você digitou {a} númerico, {b} um número decimal, {c} alfabeto.')
