class BfXpaths:
    def __init__(self):
        self.xpaths_login = {'botao_cookie':"//button[@class='cookiebanner5' and contains(text(),'Aceitar Cookies')]",
                            'aba_login':"//*[contains(text(),'Login')]",
                            'campo_email':"//input[@name='email' and @type='email']",
                            'campo_senha':"//input[@name='password' and @type='password']",
                            'botao_login':"//button[@type='submit' and contains(text(),'Login')]",
                            'botao_ultimo_jogo':"//button[contains(text(),'Jogou pela última vez')]"}
        
        self.xpaths_visao_global = {'status':"//*[@class='gold']",
                                    'botao_prenda_purpura':"//*[contains(text(), 'Prenda Purpura')]/ancestor::td//*[contains(text(),'Desembrulhar prenda')]",
                                    'botao_prenda_azul':"//*[contains(text(), 'Prenda Azul escura')]/ancestor::td//*[contains(text(),'Desembrulhar prenda')]"}
        
        self.xpaths_botoes_menu = {'botao_visao_global':"//li[@class='active']",
                                   'botao_cidade':"//a[@href[contains(.,'/city/index')]]",
                                   'botao_cacar':"//a[@href[contains(.,'/robbery/index')]]"}
        
        self.xpaths_cidade = {'botao_gruta':"//a[@href='/city/grotte']",
                              'botao_igreja':"//a[@href='/city/church']",
                              'botao_facil':"//input[@value='Fácil']",
                              'botao_medio':"//input[@value='Média']",
                              'botao_dificil':"//input[@value='Difícil']",
                              'botao_curar_igreja':"//input[@name='heal']",
                              'texto_curar_igreja':"//*[contains(text(),'Cura 100%')]"}
        
        self.xpaths_cacar = {'botao_fazenda':"//button[@class='btn' and contains(text(),'Fazenda')]",
                             'botao_aldeia':"//button[@class='btn' and contains(text(),'Aldeia')]",
                             'botao_pequena_cidade':"//button[@class='btn' and contains(text(),'Pequena cidade')]",
                             'botao_cidade_cacar':"//button[@class='btn' and normalize-space(text())='Cidade']",
                             'botao_cidade_grande':"//button[@class='btn' and contains(text(),'Grande Cidade')]",
                             'botao_pvp':"//input[@class='btn' and @type='submit' and @name='optionsearch']",
                             'botao_atacar':"//button[contains(text(), 'Atacar') and @class='btn' and @type='submit']",
                             'texto_resultado_cacar':"//div[@class='buildingDesc']",
                             'texto_resultado_pvp':"//h3[contains(text(),'Vencedor')]",
                             'ouro_pvp_venceu':"//p[@class='gold']",
                             'ouro_pvp_perdeu':"//p[@class='gold' and contains(text(),'Perda efetiva')]"}
        
        self.xpaths_botoes_voltar = {'botao_repetir':"//button[@class='btn' and @type='submit' and contains(text(),'Repetir')]",
                                     'botao_regressar':"//a[@class='btn' and contains(text(),'regressar')]"}