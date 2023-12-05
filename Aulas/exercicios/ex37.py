n = int(input('Informe um número decimal: '))
opcao = int(input('Informe a opção desejada:\n1 - Converter em \033[1mBinário\033[m.\n2 - Converter em \033[31mOctal\033[m.\n3 - Converter em \033[34mHexadecimal\033[m\nDigite uma opção: '))
if opcao == 1:
    numero = bin(n)
    tipo = '\033[1mBinário\033[m'
elif opcao == 2:
    numero = oct(n)
    tipo = '\033[31mOctal\033[m'
elif opcao == 3:
    numero = hex(n)
    tipo = '\033[34mHexadecimal\033[m'
else:
    print('Opção inválida')
print(f'O número {n} em {tipo} é: {numero[2:]}')
