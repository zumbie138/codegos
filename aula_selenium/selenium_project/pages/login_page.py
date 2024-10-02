import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.error_message_login = (By.XPATH,"//*[@data-test='error']")
        
    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
        
    def verificar_mensagem_erro_login(self):
        self.verificar_se_elemento_existe(self.error_message_login)