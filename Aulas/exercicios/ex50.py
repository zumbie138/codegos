soma = 0
for i in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n%2 == 0:
        soma+=n
print(f'A soma dos números digitados é: \033[33m{soma}\033[m')