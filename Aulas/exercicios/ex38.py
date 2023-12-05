n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print(f'O \033[1;33mprimeiro\033[m número {n1} é maior!')
elif n2 > n1:
    print(f'O \033[1;33msegundo\033[m número {n2} é maior!')
elif n1 == n2:
    print(f'Os números são \033[1;33miguais\033[m!')
else:
    print(f'\033[31mHouve algum erro de digitação\033[m')