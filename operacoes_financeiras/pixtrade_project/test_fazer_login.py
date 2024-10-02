import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from iniciar_navegador import setup_teardown

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestLogin:
    def test_login_valido(self):
        
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login()
        
        home_page.verificar_login_com_sucesso()
        