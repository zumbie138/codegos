from selenium import webdriver
from selenium.webdriver.common.by import By

olymptrade = 'https://olymptrade.com/pt-br'
pixtrade = 'https://pixtrade.io/'
pocket_option = 'https://pocketoption.com/pt/login/'
qxbroker = 'https://qxbroker.com/pt'

driver:webdriver.Remote

def iniciar_navegador(link):
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(link)

def fechar_navegador():
    global driver
    driver.quit()

def teste_olymptrade():
    global driver
    assert driver.find_element(By.XPATH, "//span[@class='kzbPUgX-ru' and contains(text(),'Permitir Todos os Cookies')]"), 'deu errado'
    assert driver.find_element(By.XPATH, "//button[@data-trans='home_start_trading' and @data-test ='home-page-welcome']"), 'deu errado'

    botao_cookie = driver.find_element(By.XPATH, "//button[@data-test='cookie_popup_close']")
    botao_inicio = driver.find_element(By.XPATH, "//button[@data-trans='home_start_trading' and @data-test ='home-page-welcome']")

    botao_cookie.click()
    botao_inicio.click()

def teste_pixtrade():
    global driver
    botao_comeceinvestir = driver.find_elements(By.XPATH, "//*[contains(text(),'COMECE A INVESTIR')]")
    botao_comeceinvestir[0].click()

def teste_pocket_option():
    global driver
    botao_registar = driver.find_element(By.XPATH,"//a[contains(text(),'Registrar-se')]")
    botao_registar.click()
    
def teste_qxbroker():
    global driver
    botao_registar = driver.find_element(By.XPATH,"//a[@class='main__platform-button']")
    botao_registar.click()
    
# iniciar_navegador(olymptrade)
# teste_olymptrade()

# iniciar_navegador(pixtrade)
# teste_pixtrade()

# iniciar_navegador(pocket_option)
# teste_pocket_option()

iniciar_navegador(qxbroker)
teste_qxbroker()
