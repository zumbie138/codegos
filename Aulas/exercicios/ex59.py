n1 = float(input('Informe um número: '))
n2 = float(input('Informe um número: '))
escolha = ''
while escolha !='5':
    print('\033[33m[ 1 ] \033[m\033[34mSOMA\033[m')
    print('\033[33m[ 2 ] \033[m\033[34mMULTIPLICAR\033[m')
    print('\033[33m[ 3 ] \033[m\033[34mMAIOR\033[m')
    print('\033[33m[ 4 ] \033[m\033[34mNOVOS NÚMEROS\033[m')
    print('\033[33m[ 5 ] \033[m\033[34mSAIR\033[m')
    escolha = str(input('Coloque o valor desejado: '))
    if escolha == '1':
        resultado = n1+n2
    elif escolha == '2':
        resultado = n1*n2
    elif escolha == '3':
        if n1>n2:
            print(f'maior: {n1}')
        else:
            print(f'maior: {n2}')
    elif escolha == '4':
        resultado = n1+1
    else:
        print('Número inválido!')