import racas
import monstros
from random import randint
from time import sleep
# import itens
#from sys import exit

nome = ''
raca = ''
classe = ''
level = 0
experiencia_total = 0
forca = 0
agilidade = 0
vitalidade = 0
inteligencia = 0
carisma = 0
dano = 0
defesa = 0
vida = 0
vida_t = 0
gold = 0
inventario = {}
selecao_aventura = {'campo':{'cobra':40,'lobo':25,'urso':20,'troll':15},'caverna':{'rato':40,'morcego':25,'aranha':20,'troll':15},'cemiterio':{'rato_zumbi':40,'cobra':25,'aranha':20,'troll':15}}
def criar_personagem():
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    selecao_classe={'Humano':{'1':'guerreiro','2':'mago','3':'clerigo'},
                'Elfo':{'1':'ranger','2':'feiticeiro','3':'druida'},
                'Orc':{'1':'barbaro','2':'bruxo','3':'shaman'}}
    selecao_raca={'1':'Humano','2':'Elfo','3':'Orc'}
    print('!!TELA DE CRIAÇÃO DE PERSONAGEM!!')
    nome = str(input('Coloque o nome do seu personagem: '))
    escolha_raca = str(input('Escolha sua raça: \n [ 1 ] - Humano.\n [ 2 ] - Elfo.\n [ 3 ] - Orc.\n'))
    raca = selecao_raca[escolha_raca]
    escolha_raca = str(input(f'Escolha sua classe: \n [ 1 ] - {selecao_classe[raca]["1"].title()}.\n [ 2 ] - {selecao_classe[raca]["2"].title()}.\n [ 3 ] - {selecao_classe[raca]["3"].title()}.\n'))
    classe = selecao_classe[raca][escolha_raca]
    personagem = getattr(racas,raca)(nome,forca,agilidade,vitalidade,inteligencia,carisma,level)
    raca_classe = getattr(personagem, classe)
    raca_classe()
    forca = personagem.forca
    agilidade = personagem.agilidade
    vitalidade = personagem.vitalidade
    inteligencia = personagem.inteligencia
    carisma = personagem.carisma
    dano = personagem.dano
    defesa = personagem.defesa
    vida = personagem.vida
    vida_t = personagem.vida
    level = personagem.level
    print(f'O {nome} é um {raca} da classe {classe} e esta no level {level}.\nForça: {forca}\nAgilidade: {agilidade}\nVitalidade: {vitalidade}\nInteligencia: {inteligencia}\nCarisma:{carisma}\nDano/Defesa: {dano}/{defesa}\nVida: {vida}/{vida_t}.')
    
def continuar_aventura():
    print('recurso ainda nao disponivel')

def dormir():
    global nome, raca, classe, level, experiencia_total, forca, agilidade, vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    print("Você começa a dormir !")
    while vida < vida_t:
        cura = randint(0,2)
        vida = vida + cura
        print(f'Voce dorme profundamente e cura {cura} pontos de vida\n Vida: {vida:.2f}/{vida_t}')
        sleep(2.5)
        if vida > vida_t:
            diferenca = vida - vida_t
            vida = vida - diferenca
    print('Voce recuperou toda vida, está saudável agora')

def treinar():
    print("Você começa a treinar!")
    refugio()

def armario():
    escolha = str(input('[ 1 ] Ver mochila.\n[ 2 ] Ver armário\n [ 3 ] Voltar.'))

def espelho():
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    print(f'Você se olha no espelho e vê:\nSeu level é {level} você é um {raca} da classe {classe}\nForça: {forca}\nAgilidade: {agilidade}\nVitalidade: {vitalidade}\nInteligencia: {inteligencia}\nCarisma:{carisma}\nDano/Defesa: {dano}/{defesa}\nVida: {vida}/{vida_t}.')
    input('Pressione qualquer tecla para voltar: ')
    refugio()

def refugio():
    escolha = input('Bem Vindo a sua casa, oque deseja fazer?\n[ 1 ] Dormir.\n[ 2 ] Treinar.\n[ 3 ] Armário.\n[ 4 ] Olhar no espelho\n [ 5 ] Voltar.')
    if escolha == '1':
        dormir()
    elif escolha == '2':
        treinar()
    elif escolha == '3':
        armario()
    elif escolha == '4':
        espelho()

def cidade():
    escolha = input('Bem vindo a cidade, onde deseja ir?\n[ 1 ] Taverna\n[ 2 ] Lojas\n[ 3 ] Ferreiro')   

def criatura_aleatória():
    selecao_aventura = {'campo':{'cobra':40,'lobo':25,'urso':20,'troll':15},'caverna':{'rato':40,'morcego':25,'aranha':20,'troll':15},'cemiterio':{'rato_zumbi':40,'cobra':25,'aranha':20,'troll':15}}
    escolha_aventura = {'1':'campo','2':'caverna','3':'cemiterio'}
    escolha = str(input('Escolha o local que deseja se aventurar:\n[ 1 ] Campos\n[ 2 ] Cavernas\n[ 3 ] Cemitério\n[ 4 ] Voltar'))
    if escolha == '4':
        menu_inicial()
    aventura = escolha_aventura[escolha]
    criatura_escolhida = False
    while not criatura_escolhida:
        for criatura , porcentagem in selecao_aventura[aventura].items():
            porcentagem_definida = randint(0,100)
            if porcentagem_definida <= porcentagem:
                criatura_escolhida = criatura
                return criatura_escolhida

def importar_criatura(criatura):
    classe_criatura = monstros.Criaturas()
    funcao_criatura = getattr(classe_criatura, criatura)
    funcao_criatura()
    forca_criatura = classe_criatura.forca_c
    agilidade_criatura = classe_criatura.agilidade_c
    vitalidade_criatura = classe_criatura.vitalidade_c
    inteligencia_criatura = classe_criatura.inteligencia_c
    carisma_criatura = classe_criatura.carisma_c
    vida_criatura = classe_criatura.vida_c
    vida_criatura_t = classe_criatura.vida_c
    dano_criatura = classe_criatura.dano_c
    defesa_criatura = classe_criatura.defesa_c
    experiencia_criatura = classe_criatura.experiencia_c
    print(f'O monstro {criatura.title()} apareceu:\nVida: {vida_criatura}/{vida_criatura_t}')
    return vida_criatura, vida_criatura_t, dano_criatura, defesa_criatura, forca_criatura, agilidade_criatura, vitalidade_criatura, inteligencia_criatura, carisma_criatura, experiencia_criatura

def subir_nivel():
#vida 0, vida_t 1, dano 2, defesa 3, forca 4, agilidade 5, vitalidade 6, inteligencia 7,carisma 8, level 9, experiencia_total 10, , nome11, raca12, classe 13  
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    personagem = getattr(racas,raca)(nome,forca,agilidade,vitalidade,inteligencia,carisma,level)
    raca_classe = getattr(personagem, classe)
    raca_classe()
    forca = personagem.forca
    agilidade = personagem.agilidade
    vitalidade = personagem.vitalidade
    inteligencia = personagem.inteligencia
    carisma = personagem.carisma
    dano = personagem.dano
    defesa = personagem.defesa
    vida = personagem.vida
    vida_t = personagem.vida
    level = personagem.level
    print(f'Seu personagem subiu para o nível {level}.')
    
def verificar_level():
    tabela_experiencia = {1:100,2:400,3:1000,4:1800,5:2800,6:4000,7:7500,8:10000}
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    if tabela_experiencia[level] <= experiencia_total:
        subir_nivel() 
#vida 0, vida_t 1, dano 2, defesa 3, forca 4, agilidade 5, vitalidade 6, inteligencia 7,carisma 8, level 9, experiencia_total 10, , nome11, raca12, classe 13  
        

def batalha(criatura):
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    caracteristicas_criatura = importar_criatura(criatura)
    vida_criatura = caracteristicas_criatura[0]
    vida_criatura_t = caracteristicas_criatura[1]
    dano_criatura = caracteristicas_criatura[2]
    defesa_criatura = caracteristicas_criatura[3]
    experiencia_criatura = caracteristicas_criatura[9]  
    while vida > 0:
        dano_rand = randint(0,3)
        dano_rand_criatura = randint(0,3)
        ataque_heroi = dano*0.7+dano_rand*0.3 - (defesa_criatura/10)
        ataque_criatura = dano_criatura*0.7+dano_rand_criatura*0.3 - (defesa/10)
        vida = vida - ataque_criatura
        vida_criatura = vida_criatura - ataque_heroi
        print(f'Você causou \033[31m{ataque_heroi:.2f}\033[m de dano no inimigo.\nVida do inimigo: {vida_criatura:.2f}/{vida_criatura_t}')
        print(f'O inimigo causou \033[31m{ataque_criatura:.2f}\033[m em você.\nVida do Herói: {vida:.2f}/{vida_t}')
        sleep(1)
        if vida_criatura <= 0:
            print(f'Criatura derrotada !\nGanhou {experiencia_criatura} de experiência!')
            experiencia_total += experiencia_criatura
            print(f'Agora possui um total de {experiencia_total} de experiência!')
            verificar_level()
            aventura()
        
    print('Você está fraco demais para continuar')
    refugio()
        
    

def aventura():
    criatura_escolhida = criatura_aleatória()
    print(f'A criatura que você irá enfrentar é {criatura_escolhida}')
    batalha(criatura_escolhida)
        
        
        
         
def menu_inicial():
    while True:
        escolha = str(input('Qual dessas opçôes deseja fazer: \n[ 1 ] Refúgio.\n[ 2 ] Cidade\n[ 3 ] Aventuras\n[ 4 ] Sair.'))
        if escolha == '1':
            refugio()
        elif escolha == '2':
            cidade()
        elif escolha == '3':
            aventura()
        elif escolha == '4':
            menu()
def menu():
    while True:
        escolha_menu = str(input('Oque deseja?\n{ 1 } - Criar novo personagem.\n{ 2 } - Continuar personagem salvo.\n{ 3 } - Sair.\nEscolha uma opção: '))
        if escolha_menu == '1':
            criar_personagem()
            menu_inicial()
        elif escolha_menu == '2':
            continuar_aventura()
        elif escolha_menu == '3':
            break
        else:
            print('Escolha inválida')
            
menu()