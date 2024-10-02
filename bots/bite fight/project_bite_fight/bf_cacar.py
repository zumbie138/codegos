from selenium.webdriver.common.by import By
from bf_base import BasePage
from bf_xpaths import BfXpaths
import bf_iniciar
import re

class PageCacar(BasePage):
    def __init__(self):
        self.driver = bf_iniciar.driver
        self.xpaths = BfXpaths()
        self.botao_cacar = (By.XPATH, self.xpaths.xpaths_botoes_menu['botao_cacar'])
        self.botao_repetir = (By.XPATH, self.xpaths.xpaths_botoes_voltar['botao_repetir'])
        self.botao_regressar = (By.XPATH, self.xpaths.xpaths_botoes_voltar['botao_regressar'])
        self.botao_pvp = (By.XPATH, self.xpaths.xpaths_cacar['botao_pvp'])
        self.botao_atacar = (By.XPATH, self.xpaths.xpaths_cacar['botao_atacar'])
        self.texto_status = (By.XPATH, self.xpaths.xpaths_visao_global['status'])
        self.texto_resultado = (By.XPATH, self.xpaths.xpaths_cacar['texto_resultado_cacar'])
        self.texto_resultado_pvp = (By.XPATH, self.xpaths.xpaths_cacar['texto_resultado_pvp'])
        self.ouro_pvp_venceu = (By.XPATH, self.xpaths.xpaths_cacar['ouro_pvp_venceu'])
        self.ouro_pvp_perdeu = (By.XPATH, self.xpaths.xpaths_cacar['ouro_pvp_perdeu'])
        self.sangue = self.ouro = self.experiencia = 0

    def cacar_humanos(self,local,string_local):
        self.clicar(self.botao_cacar)
        botao_local_caca = (By.XPATH, self.xpaths.xpaths_cacar[local])
        quantidade = self.numero_loop(string_local)
        self.clicar(botao_local_caca)
        print(f'A 1ª caçada foi bem sucedida !')
        for i in range(quantidade-1):
            if self.status_teste(self.texto_status):
                self.espera_explicita_clicavel(self.botao_regressar)
                self.driver.implicitly_wait(0.1)
                len_element = len(self.encontrar_elementos(self.botao_repetir))
                self.driver.implicitly_wait(15)
                if len_element > 0:
                    self.extrair_texto_resultado_caca()
                    print(f'A {i+2}ª caçada foi bem sucedida !')
                    self.clicar(self.botao_repetir)
                else:
                    print(f'A {i+2}ª caçada falhou !')
                    self.clicar(self.botao_regressar)
                    self.esperar_clicar(botao_local_caca)
            else:
                print('Não possui mais pontos de energia ou vida para continuar.')
                break
        print(f'No total você saqueou {self.sangue} de sangue, {self.ouro} de ouro e {self.experiencia} de experiência.')
        self.sangue = self.ouro = self.experiencia = 0
        self.esperar_clicar(self.botao_regressar)
                  
    def extrair_texto_resultado_caca(self):
        texto_resultado = self.extrair_texto(self.texto_resultado)
        if 'A tua caçada leva-te até' in texto_resultado or 'tua caçada levou-te' in texto_resultado:
            sangue = int(re.search(r'Capturaste\s+(.*?)\s+Sangue', texto_resultado).group(1).replace('.','').strip())
            ouro = int(re.search(r'Sangue,\s+(.*?)\s+ouro', texto_resultado).group(1).replace('.','').strip())
            experiencia = int(re.search(r'(\d+)\s+pontos\s+de\s+experiência!',texto_resultado).group(1).strip())
            print(f'Ouro: {ouro} Sangue: {sangue} Experiência: {experiencia}')
            self.ouro = self.ouro + ouro
            self.sangue = self.sangue + sangue
            self.experiencia = self.experiencia + experiencia
        else:
            print('Não saqueou nada!!')

    def cacar_pvp(self):
        vitoria = derrota = ouro_vitoria = ouro_derrota = 0
        quantidade = self.numero_loop('no pvp')
        self.clicar(self.botao_cacar)
        for i in range(quantidade):
            if self.status_teste(self.texto_status):
                self.esperar_clicar(self.botao_pvp)
                self.esperar_clicar(self.botao_atacar)
                print(f'Atacou pela {i+1}ª vez:')
                resultado_pvp = self.extrair_texto(self.texto_resultado_pvp)
                print(resultado_pvp)
                if 'Zumbie138' in resultado_pvp:
                    ouro = self.pegar_numero_vitoria(self.ouro_pvp_venceu)
                    print(f'+{ouro}')
                    ouro_vitoria += ouro
                    vitoria += 1
                else:
                    ouro = self.pegar_numero_derrota(self.ouro_pvp_perdeu)
                    print(f'-{ouro}')
                    ouro_derrota += ouro
                    derrota += 1
                self.esperar_clicar(self.botao_regressar)
            else:
                print('Não possui mais pontos de energia ou vida para continuar.')
                break
        print(f'Você venceu {vitoria} vezes, e perdeu {derrota} vezes!')
        resultado = ouro_vitoria - ouro_derrota
        if resultado > 0:
            print(f'E você ganhou {resultado} de ouro total')
        else:
            print(f'E você perdeu {resultado} de ouro total')
        
    
    
