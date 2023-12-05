homem_dict = {}
mulher_dict = {}
vetor_idade = []
vetor_idade_mulher = []
contador = 0
for i in range(1,5):
    nome = str(input(f'Informe o {i}ª nome: '))
    idade = int(input(f'Informe a {i}ª idade: '))
    sexo = str(input(f'Informe o {i}ª gênero:\n1 - Homem.\n2 - Mulher.\nQual opção? '))
    vetor_idade.append(idade)
    if sexo == '1':
        homem = {idade:nome}
        homem_dict.update(homem)
    elif sexo == '2':
        mulher = {idade:nome}
        mulher_dict.update(mulher)
        vetor_idade_mulher.append(idade)
media = sum(vetor_idade)/len(vetor_idade)
maior_idade = max(vetor_idade)
nome_velho = homem_dict[maior_idade]
for idade_mulher in vetor_idade_mulher:
    if idade_mulher <= 20:
        contador+=1
print(f'A \033[34mmédia de idade\033[m do grupo é \033[1m{media}\033[m anos.\nO homem \033[34mmais velho\033[m se chama \033[1m{nome_velho}\033[m.\nExistem \033[1m{contador}\033[m mulheres com \033[34mmenos de 20\033[m anos.')