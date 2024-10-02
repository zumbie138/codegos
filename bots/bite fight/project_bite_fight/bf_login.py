from selenium.webdriver.common.by import By
from bf_xpaths import  BfXpaths
from bf_base import BasePage
import bf_iniciar

class LoginPage(BasePage):
    def __init__(self):
        self.email = 'gabriel.mks@gmail.com'
        self.senha = 'Leproso.66'
        self.driver = bf_iniciar.driver
        xpaths = BfXpaths()
        self.aba_login = (By.XPATH, xpaths.xpaths_login['aba_login'])
        self.campo_email = (By.XPATH, xpaths.xpaths_login['campo_email'])
        self.campo_senha = (By.XPATH, xpaths.xpaths_login['campo_senha'])
        self.botao_cookie = (By.XPATH, xpaths.xpaths_login['botao_cookie'])
        self.botao_login = (By.XPATH, xpaths.xpaths_login['botao_login'])
        self.botao_ultimo_jogo = (By.XPATH, xpaths.xpaths_login['botao_ultimo_jogo'])
        self.texto_status = (By.XPATH,xpaths.xpaths_visao_global['status'])
        
    def fazer_login(self):
        self.clicar(self.botao_cookie)
        self.clicar(self.aba_login)
        self.escrever(self.campo_email,self.email)
        self.escrever(self.campo_senha,self.senha)
        self.clicar(self.botao_login)
        self.esperar_clicar(self.botao_ultimo_jogo)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.espera_explicita_visivel(self.texto_status)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        
    def chamar_status(self):
        texto_status = self.extrair_texto(self.texto_status)
        vetor_string = texto_status.split()
        print("STATUS DO VAMPIRO")
        print(f'Ouro: {vetor_string[0]}\nPedras do Inferno: {vetor_string[1]}\nFragmentos: {vetor_string[2]}\nPontos de ação: {vetor_string[3]}/{vetor_string[5]}\nEnergia: {vetor_string[6]}/{vetor_string[8]}\nNível: {vetor_string[9]}\nValor de batalha: {vetor_string[10]}')
        
    