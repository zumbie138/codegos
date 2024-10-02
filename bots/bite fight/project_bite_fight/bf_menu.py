import bf_iniciar
from bf_login import LoginPage
from bf_cacar import PageCacar
from bf_cidade import PageCidade

bf_iniciar.iniciar_navegador()
login = LoginPage()
cacar = PageCacar()
cidade = PageCidade()
login.fazer_login()

def menu_caca_humano():
    opcoes = {'1': ('botao_fazenda', 'na Fazenda'),
                '2': ('botao_aldeia', 'na Aldeia'),
                '3': ('botao_pequena_cidade', 'na Pequena Cidade'),
                '4': ('botao_cidade_cacar', 'na Cidade'),
                '5': ('botao_cidade_grande', 'na Cidade Grande')}
    while True:
        escolha = input('Coloque a opção desejada:\n[ 1 ] - Fazenda.\n[ 2 ] - Aldeia.\n[ 3 ] - Pequena Cidade.\n[ 4 ] - Cidade.\n[ 5 ] - Cidade Grande.\n[ 6 ] - Voltar.\nEscolha uma opção: ')
        if escolha == '6':
            break
        elif escolha in opcoes:
            local, string_local = opcoes[escolha]
            cacar.cacar_humanos(local, string_local)
        else:
            print('Escolha inválida.')
            
while True:
    login.chamar_status()
    escolha = input('Bem vindo ao bot do BiteFight!\n[ 1 ] - Caçar humanos.\n[ 2 ] - Caçar vampiros/lobisomens.\n[ 3 ] - Matar demônios.\n[ 4 ] - Se curar.\n[ 5 ] - Abrir presentes.\n[ 6 ] - Sair.\nSelecione a opção desejada: ')
    if escolha.isnumeric() and escolha == '1':
        menu_caca_humano()
    elif escolha.isnumeric() and escolha == '2':
        cacar.cacar_pvp()
    elif escolha.isnumeric() and escolha == '3':
        cidade.cacar_demonios()
    elif escolha.isnumeric() and escolha == '4':
        cidade.curar_igreja()
    elif escolha.isnumeric() and escolha == '6':
        bf_iniciar.fechar_navegador()
        break
    else:
        print('Escolha inválida.')
