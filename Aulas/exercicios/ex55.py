peso_vetor=[]
for i in range(1,6):
    peso = float(input(f'Informe o {i}ª peso em (kg): '))
    peso_vetor.append(peso)
maior = max(peso_vetor)
menor = min(peso_vetor)
print(f'O maior peso digitado é: \033[1m{maior}\033[m (kg)!')
print(f'O menor peso digitado é: \033[1m{menor}\033[m (kg)!')