from selenium.webdriver.common.by import By
from pages.page_base import PageBase
import iniciar_navegador
from dados_pixtrade import DadosPixtrade

class LoginPage(PageBase):
    def __init__(self):
        self.driver = iniciar_navegador.driver
        dados = DadosPixtrade()
        self.email = dados.email
        self.senha = dados.senha
        self.campo_email = (By.XPATH, dados.xpaths['campo_email'])
        self.campo_senha = (By.XPATH, dados.xpaths['campo_senha'])
        self.botao_entrar = (By.XPATH, dados.xpaths['botao_entrar'])
        
    def fazer_login(self):
        self.escrever(self.campo_email, self.email)
        self.escrever(self.campo_senha, self.senha)
        self.clicar(self.botao_entrar)