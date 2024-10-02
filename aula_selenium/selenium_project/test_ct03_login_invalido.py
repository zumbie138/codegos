import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_invalido
class TestCT02:
    def test_ct02_login_valido(self):
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()
        
        # Faz login
        login_page.fazer_login('standard_user', 'senha_errada')
        
        # Verifica se o login nao foi realizado
        login_page.verificar_mensagem_erro_login()