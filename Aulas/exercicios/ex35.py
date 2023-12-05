r1 = float(input('Digite o tamano da reta 1: '))
r2 = float(input('Digite o tamano da reta 2: '))
r3 = float(input('Digite o tamano da reta 3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Essas retas PODEM formar um triângulo')
else:
    print('Essas retas NÃO PODEM formar um triângulo')