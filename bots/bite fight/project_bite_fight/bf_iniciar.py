from selenium import webdriver

link = 'https://lobby.bitefight.gameforge.com/pt_BR/'
driver:webdriver.Remote        

def iniciar_navegador():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(link)

def fechar_navegador():
    global driver
    driver.quit()