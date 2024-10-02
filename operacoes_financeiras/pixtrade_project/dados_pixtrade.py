
class DadosPixtrade():
    def __init__(self):
        self.xpaths = {'campo_email':"//input[@placeholder='E-mail']",
                       'campo_senha':"//input[@placeholder='Senha']",
                       'botao_entrar':"//button[@class='css-1shdco1 e1qay7kl0']",#//button[@data-test-id='login-submit-button']
                       'botao_negociar':"//button[@data-test-id='header-trade-button']"}
        
        self.email = 'gabriel.mks@gmail.com'
        self.senha = 'Leproso.66'