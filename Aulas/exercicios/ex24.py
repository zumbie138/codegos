cidade = str(input('Informe o nome da cidade: '))
cidade_v = cidade.split()
if 'Santo' in cidade_v[0]:
    print('Sim, ela começa com Santo')
else:
    print('Não, ela não começa com Santo')