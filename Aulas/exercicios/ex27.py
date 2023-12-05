nome = str(input('Escreva seu nome completo: '))
nome_v=nome.split()
num=len(nome_v)
print(f'Primeiro nome: {nome_v[0]}\nÚltimo nome: {nome_v[num-1]}')