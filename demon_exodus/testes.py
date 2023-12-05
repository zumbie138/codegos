from random import randint
while True:
    selecao_aventura = {'campo':{'cobra':40,'lobo':25,'urso':20,'troll':15},'caverna':{'rato':40,'morcego':25,'aranha':20,'troll':15},'cemiterio':{'rato zumbi':40,'cobra':25,'aranha':20,'troll':15}}
    escolha_aventura = {'1':'campo','2':'caverna','3':'cemiterio'}
    escolha = str(input('Escolha o local que deseja se aventurar:\n[ 1 ] Campos\n[ 2 ] Cavernas\n[ 3 ] Cemitério'))
    aventura = escolha_aventura[escolha]
    criatura_escolhida = False
    while not criatura_escolhida:
        for criatura , porcentagem in selecao_aventura[aventura].items():
            porcentagem_definida = randint(0,100)
            if porcentagem_definida <= porcentagem:
                criatura_escolhida = criatura
                break
    print(criatura)