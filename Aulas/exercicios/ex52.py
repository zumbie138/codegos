from sys import exit
n = int(input('Digite um número inteiro: '))
for i in range (1, n-1):
    if n%(n-i) == 0:
        print(f'O número {n} \033[31mNÃO É PRIMO!\033[m')
        exit()
print(f'O número {n} \033[32mÉ PRIMO!\033[m')