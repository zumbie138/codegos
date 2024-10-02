from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from dados_pixtrade import DadosPixtrade
import iniciar_navegador

class HomePage(PageBase):
    def __init__(self):
        dados = DadosPixtrade()
        self.driver = iniciar_navegador.driver
        self.botao_negociar = (By.XPATH, dados.xpaths['botao_negociar'])
    
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.botao_negociar)