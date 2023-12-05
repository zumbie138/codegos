nome = str(input('Escreva seu nome completo: ')).strip()
nome_v = nome.split()
nome_sem_espaco = nome.replace(' ','')
print(f'{nome}\n{nome.upper()}\n{nome.lower()}\n{len(nome_sem_espaco)}\n{len(nome_v[0])}')