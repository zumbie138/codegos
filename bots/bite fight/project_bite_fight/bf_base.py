import bf_iniciar
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class BasePage:
    def __init__(self):
        self.driver = bf_iniciar.driver
    
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self,locator):
        return self.driver.find_elements(*locator)
    
    def espera_explicita_clicavel(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((locator)))
    
    def espera_explicita_visivel(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator)))
    
    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)
    
    def clicar(self,locator):
        self.encontrar_elemento(locator).click()
        
    def extrair_texto(self, locator):
        return self.encontrar_elemento(locator).text
    
    def esperar_clicar(self,locator):
        self.espera_explicita_clicavel(locator).click()
        
    def numero_loop(self,string_local):
        while not (quantidade := input(f'Quantas vezes deseja caçar {string_local}? ')).isnumeric():
            print('ERRO\nDigite um valor numérico.')
        return int(quantidade)
    
    def pegar_numero_derrota(self, locator):
        texto_ouro = self.extrair_texto(locator)
        return int(re.search(r'efetiva\s+\(\w+\)\s+:\s+([\d.]+)\s+Ouro',texto_ouro).group(1).replace('.','').strip())
    
    def pegar_numero_vitoria(self, locator):
        texto_ouro = self.extrair_texto(locator)
        ouro_vetor = re.findall(r'\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\b',texto_ouro)
        return int(ouro_vetor[0].replace('.','').strip()) + int(ouro_vetor[1].replace('.','').strip())
    
    def extrair_pontosacao_energia(self,locator):
        texto_status = self.extrair_texto(locator)
        vetor_string = texto_status.split()
        pontos_acao = int(vetor_string[3])
        energia = int(vetor_string[6].replace('.',''))
        return pontos_acao, energia
    
    def status_teste(self,locator):
        pontos_acao, energia = self.extrair_pontosacao_energia(locator)
        if pontos_acao > 0 and energia > 10000:
            return True
        else:
            return False