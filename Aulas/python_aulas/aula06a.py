a=True
while a:
    n1 = input('Digite um Valor ')
    n2 = input('Digite outro Valor ')
    if n1.isnumeric() and n2.isnumeric():
        if n1.isdecimal() and n2.isdecimal():
            n1=int(n1)
            n2=int(n2)
            n=n1+n2
            print(f'O resultado da soma entre {n1} e {n2} é: {n} !')
            a=False
        else:
            print('Digitou incorretamente')
    else:
        print('Digitou incorretamente')
        