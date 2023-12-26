import racas
import monstros
from random import randint,uniform
from time import sleep
import json
import os
import itens

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

def zerar_valores():
    global nome,raca,classe,level,experiencia_total,forca,agilidade,vitalidade,inteligencia,carisma,dano,defesa,vida,vida_t,inventario,gold    
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

def salvar_personagem():
    global nome,raca,classe,level,experiencia_total,forca,agilidade,vitalidade,inteligencia,carisma,dano,defesa,vida,vida_t,inventario,gold
    caminho_raiz = os.getcwd()
    caminho_save = f'{caminho_raiz}\\save'
    if not os.path.exists(caminho_save):
        os.makedirs(caminho_save)
    personagem_salvo = {'nome':nome,'raça':raca,'classe':classe,'level':level,'experiencia':experiencia_total,'força':forca,'agilidade':agilidade,'vitalidade':vitalidade,'inteligencia':inteligencia,'carisma':carisma,'dano':dano,'defesa':defesa,'vida':vida,'vida total':vida_t,'inventario':inventario,'gold':gold}
    nome_save = f'{caminho_save}\\{nome}.json'
    with open(nome_save,'w') as arquivo:
        json.dump(personagem_salvo, arquivo)
      
def criar_personagem():
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    zerar_valores()
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
    global nome,raca,classe,level,experiencia_total,forca,agilidade,vitalidade,inteligencia,carisma,dano,defesa,vida,vida_t,inventario,gold
    zerar_valores()
    caminho_saves = f'{os.getcwd()}\\save'
    saves_disponiveis = [f for f in os.listdir(caminho_saves) if f.endswith('.json')]
    for i, save in enumerate(saves_disponiveis, 1):
        print(f'[{i}] {save}')
    escolha_save = input('Qual progresso deseja acessar? ')
    if escolha_save.isdigit():
        indice = int(escolha_save) - 1
        if 0 <= indice < len(saves_disponiveis):
            save_escolhido = saves_disponiveis[indice]
            caminho_save = os.path.join(caminho_saves,save_escolhido)
            with open(caminho_save, 'r') as arquivo:
                personagem_carregado = json.load(arquivo)
                nome = personagem_carregado['nome']
                raca = personagem_carregado['raça']
                classe = personagem_carregado['classe']
                level = personagem_carregado['level']
                experiencia_total = personagem_carregado['experiencia']
                forca = personagem_carregado['força']
                agilidade = personagem_carregado['agilidade']
                vitalidade = personagem_carregado['vitalidade']
                inteligencia = personagem_carregado['inteligencia']
                carisma = personagem_carregado['carisma']
                dano = personagem_carregado['dano']
                defesa = personagem_carregado['defesa']
                vida = personagem_carregado['vida']
                vida_t = personagem_carregado['vida total']
                gold = personagem_carregado['gold']
                inventario = personagem_carregado['inventario']
                menu_inicial()
        else:
            print('Escolha inválida')
    else:
        print('Escolha inválida.')
                
def dormir():
    global nome, raca, classe, level, experiencia_total, forca, agilidade, vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    print("Você começa a dormir !")
    while vida < vida_t:
        cura = randint(1,5)
        vida = vida + cura + vitalidade
        print(f'Voce dorme profundamente e cura \033[32m{cura}\033[m pontos de vida\n Vida: {vida:.2f}/{vida_t}')
        sleep(2.5)
        if vida > vida_t:
            diferenca = vida - vida_t
            vida = vida - diferenca
    print('Voce recuperou toda vida, está saudável agora')

def treinar():
    global nome,raca,classe,level,experiencia_total,forca,agilidade,vitalidade,inteligencia,carisma,dano,defesa,vida,vida_t,inventario,gold    
    tipo_treino = str(input('Oque você deseja treinar?\n[ 1 ] Força\n[ 2 ] Agilidade\n[ 3 ] Vitalidade\n[ 4 ] Inteligência\n[ 5 ] Carisma\n[ 6 ] Voltar'))
    quantidade_treino = int(input('Quantas vezes deseja treinar? '))
    for i in range(quantidade_treino):
        if vida > 0:
            if tipo_treino == '1':
                treino = uniform(0, 0.2)
                print(f'Você começa a fazer musculação...\nVocê evoluiu {treino:.2f} pontos de força',end='\r')
                forca = forca + treino
                vida = vida - 10
                sleep(1)
            elif tipo_treino == '2':
                treino = uniform(0, 0.2)
                print(f'Você começa a pratica reflexos...\nVocê evoluiu {treino:.2f} pontos de agilidade',end='\r')
                agilidade = agilidade + treino
                vida = vida - 10
                sleep(1)
            elif tipo_treino == '3':
                treino = uniform(0, 0.2)
                print(f'Você começa a fazer correr...\nVocê evoluiu {treino:.2f} pontos de vitalidade',end='\r')
                vitalidade = vitalidade + treino
                vida = vida - 10
                sleep(1)
            elif tipo_treino == '4':
                treino = uniform(0, 0.2)
                print(f'Você começa a fazer estudar...\nVocê evoluiu {treino:.2f} pontos de inteligência',end='\r')
                inteligencia = inteligencia + treino
                vida = vida - 10
                sleep(1)
            elif tipo_treino == '5':
                treino = uniform(0, 0.2)
                print(f'Você começa a praticar discurso...\nVocê evoluiu {treino:.2f} pontos de carisma',end='\r')
                forca = forca + treino
                vida = vida - 10
                sleep(1)
            elif tipo_treino == '6':
                refugio()
            else:
                print('Opção de treino inválida.')
                treinar()
        else:
            print('Você está com a vida baixa, vá descansar.')
            break
    refugio()

def armario():
    global inventario
    escolha = str(input('[ 1 ] Ver mochila.\n[ 2 ] Ver armário\n[ 3 ] Voltar.'))
    if escolha == '1':
        print(f'{inventario}')
    elif escolha == '2':
        print(f'{inventario}')
    elif escolha == '3':
        refugio()
    else:
        print('Escolha inválida.')
        armario()
    
    
def espelho():
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    print(f'Você se olha no espelho e vê:\nSeu level é {level} você é um {raca} da classe {classe}\nForça: {forca:.2f}\nAgilidade: {agilidade:.2f}\nVitalidade: {vitalidade:.2f}\nInteligencia: {inteligencia:.2f}\nCarisma:{carisma:.2f}\nDano/Defesa: {dano:.2f}/{defesa:.2f}\nVida: {vida:.2f}/{vida_t:.2f}.')
    input('Pressione qualquer tecla para voltar: ')
    refugio()

def refugio():
    salvar_personagem()
    escolha = input('Bem Vindo a sua casa, oque deseja fazer?\n[ 1 ] Dormir.\n[ 2 ] Treinar.\n[ 3 ] Armário.\n[ 4 ] Olhar no espelho\n[ 5 ] Voltar.')
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
    espolios = classe_criatura.espolios
    print(f'O monstro \033[1m{criatura.title()}\033[m apareceu:\nVida: {vida_criatura}/{vida_criatura_t}')
    return vida_criatura, vida_criatura_t, dano_criatura, defesa_criatura, forca_criatura, agilidade_criatura, vitalidade_criatura, inteligencia_criatura, carisma_criatura, experiencia_criatura, espolios

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

def espolios_itens(espolios):
    global inventario
    for loot , porcentagem in espolios.items():
        porcentagem_definida = randint(0,100)
        if porcentagem_definida <= porcentagem:
            inventario[loot] = inventario.get(loot, 0)+1
            print(f'Você ganhou um {loot} de espólio.')

def batalha(criatura):
    global nome, raca, classe, level, experiencia_total, forca, agilidade,vitalidade, inteligencia, carisma, dano, defesa, vida, vida_t
    caracteristicas_criatura = importar_criatura(criatura)
    vida_criatura = caracteristicas_criatura[0]
    vida_criatura_t = caracteristicas_criatura[1]
    dano_criatura = caracteristicas_criatura[2]
    defesa_criatura = caracteristicas_criatura[3]
    experiencia_criatura = caracteristicas_criatura[9]  
    espolios = caracteristicas_criatura[10]
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
            espolios_itens(espolios)
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
        escolha_menu = str(input('Oque deseja?\n[ 1 ] - Criar novo personagem.\n[ 2 ] - Continuar personagem salvo.\n[ 3 ] - Sair.\nEscolha uma opção: '))
        if escolha_menu == '1':
            criar_personagem()
            menu_inicial()
        elif escolha_menu == '2':
            continuar_aventura()
        elif escolha_menu == '3':
            quit()
        else:
            print('Escolha inválida')
            
menu()