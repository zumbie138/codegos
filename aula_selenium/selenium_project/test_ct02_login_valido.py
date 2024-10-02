import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()
        
        # Faz login
        login_page.fazer_login('standard_user', 'secret_sauce')
        
        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()