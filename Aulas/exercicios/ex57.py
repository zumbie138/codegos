while True:
    sexo = str(input('Você é homem ou mulher?\nDigite: (H/M)? ')).upper()
    if sexo != 'M' and sexo != 'H':
        print('Valor inválido, digite novamente (H/M)')
    else:
        if sexo == 'M':
            frase = 'mulher'
        if sexo == 'H':
            frase = 'homem'
        print(f'Você é {frase} !')
        break