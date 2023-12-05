#\033[style;text;backm
#\033[0;33;44m
#style: 0 none; 1 bold; 4 underline; 7 negative;
#text:30 branco;31 vermelho;32 verde;33 amarelo;34 azul;35 lilas;36 azul bebe;37 cinza;
#back:40 branco;41 vermelho;42 verde;43 amarelo;44 azul;45 lilas;46 azul bebe;47 cinza;
# print('\033[32mOlá, Mundo!\033[m')
# a = 3
# b = 5
# print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')
# nome = 'Zhafyr'
# print(f'O nome do herói é \033[4;34m{nome}\033[m')
nome = 'Zhafyr'
cores = {'limpa'       :'\033[m',
         'azul'        :'\033[34m',
         'amarelo'     :'\033[33m',
         'pretoebranco':'\033[7:30m'}

print(f'O nome do herói é {cores["amarelo"]}{nome}{cores["limpa"]}')
