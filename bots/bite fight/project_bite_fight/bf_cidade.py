from bf_base import BasePage
from bf_xpaths import BfXpaths
from selenium.webdriver.common.by import By
import bf_iniciar
import re

class PageCidade(BasePage):
    def __init__(self):
        self.driver = bf_iniciar.driver
        self.xpaths = BfXpaths()
        self.botao_cidade = (By.XPATH, self.xpaths.xpaths_botoes_menu['botao_cidade'])
        self.botao_gruta = (By.XPATH, self.xpaths.xpaths_cidade['botao_gruta'])
        self.botao_igreja = (By.XPATH, self.xpaths.xpaths_cidade['botao_igreja'])
        self.botao_facil = (By.XPATH, self.xpaths.xpaths_cidade['botao_facil'])
        self.botao_medio = (By.XPATH, self.xpaths.xpaths_cidade['botao_medio'])
        self.botao_dificil = (By.XPATH, self.xpaths.xpaths_cidade['botao_dificil'])
        self.botao_curar_igreja = (By.XPATH, self.xpaths.xpaths_cidade['botao_curar_igreja'])
        self.texto_curar_igreja = (By.XPATH, self.xpaths.xpaths_cidade['texto_curar_igreja'])
        self.botao_regressar = (By.XPATH, self.xpaths.xpaths_botoes_voltar['botao_regressar'])
        self.ouro_pvp_venceu = (By.XPATH, self.xpaths.xpaths_cacar['ouro_pvp_venceu'])
        self.texto_status = (By.XPATH, self.xpaths.xpaths_visao_global['status'])
        
    def cacar_demonios(self):
        self.clicar(self.botao_cidade)
        self.esperar_clicar(self.botao_gruta)
        escolha = input('Escolha a dificuldade:\n[ 1 ] - Fácil.\n[ 2 ] - Médio.\n[ 3 ] - Difícil.\n')
        quantidade = self.numero_loop('demônios')
        for i in range(quantidade):
            if self.status_teste(self.texto_status):
                match escolha:
                    case '1':
                        self.esperar_clicar(self.botao_facil)
                    case '2':
                        self.esperar_clicar(self.botao_medio)
                    case '3':
                        self.esperar_clicar(self.botao_dificil)
                print(f'Caçou o {i+1}ª demônio')
                self.esperar_clicar(self.botao_regressar)
            else:
                print('Não possui mais pontos de energia ou vida para continuar.')
                teste_cura = self.curar_igreja()
                self.clicar(self.botao_cidade)
                self.esperar_clicar(self.botao_gruta)
                if not teste_cura:
                    break
    
    def curar_igreja(self):
        self.clicar(self.botao_cidade)
        self.esperar_clicar(self.botao_igreja)
        texto_curar = self.extrair_texto(self.texto_curar_igreja)
        cura_pa = int(re.search(r'vitalidade\s+por\s+(\d+)\s+de\s+PA', texto_curar).group(1).strip())
        pontos_acao, _ = self.extrair_pontosacao_energia(self.texto_status)
        if cura_pa < pontos_acao:
            self.esperar_clicar(self.botao_curar_igreja)
            return True
        else:
            print('Não possui PA para se curar na igreja.')
            return False
        