a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
for i in range(1, 11):
    resultado = a1 + (i - 1) * r
    print(f'a{i} = {a1} + ({i} - 1) x {r} = {resultado}')