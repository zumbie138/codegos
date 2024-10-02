from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from bs4 import BeautifulSoup as bp
import requests
from bs4 import BeautifulSoup
import re
import os
import time as tempo

class BiteFight:
    def __init__(self):
        self.link_bite_fight="https://lobby.bitefight.gameforge.com/pt_BR/"
        self.login="gabriel.mks@gmail.com"
        self.senha="Leproso.66"
        self.xpaths_site ={
            "init":{
                "usuario": '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div/input',
                "senha": '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[3]/div/input',
                "entrar": '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/p/button[1]',
                "cookie": '/html/body/div[4]/div/div/span[2]/button[2]',
                "botao":'/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]',
                "botao2":'/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/button/span'
            },
            "boton_menu":{
                "cacar": '/html/body/div[5]/div[1]/ul/li[6]/a',
                "city": '/html/body/div[5]/div[1]/ul/li[5]/a',
                "gruta":'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/a',
                "igreja": '/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[7]/td[2]/a',
                "visao_geral": '/html/body/div[5]/div[1]/ul/li[2]/a',
                "pop_up" : '/html/body/div[6]/div[2]/div/div/div[3]/div[2]/div[1]'
            },
            "buttons":{
                "return": '/html/body/div[5]/div[2]/div[3]/div/a',
                "repeat": '/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span'          
            },
            "human":{
                "fazenda": '/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/button',
                "aldeia": '/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[4]/div/button',
                "pequena_cidade": '/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[6]/div/button',
                "cidade": '/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[8]/div/button',
                "cidade_grande": '/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[10]/div/button'
            },
            "demon":{
                "facil": '/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[1]/form/div/input',
                "medio": '/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[2]/form/div/input',
                "dificil": '/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/form/div/input'
            },
            "pvp":{
                "pvp_escolha": '/html/body/div[5]/div[2]/div[3]/div[1]/div[2]/div/form[1]/div/div/div/input',
                "pvp_ataque": '/html/body/div[5]/div[2]/div[4]/div[2]/div/div[2]/table/tbody/tr[9]/td/table/tbody/tr/td[1]/form/div/div/button'
            },
            "curar":{
                "curar_igreja": '/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/form/div/div/input',
                "curar_pocao": '/html/body/div[5]/div[2]/div[5]/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/a',
                "presente_ouro": '/html/body/div[5]/div[2]/div[6]/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/a',
                "presente_energia": '/html/body/div[5]/div[2]/div[6]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td[2]/div/div/a'
            }            
        }
        self.drive = webdriver.Firefox()
        self.drive.maximize_window()
        
    def clicar_elemento(self,patt1):
        try:
            clicar=WebDriverWait(self.drive,10).until(EC.element_to_be_clickable((By.XPATH, patt1)))
            clicar.click()
        except:
            self.chamar_menu()
        
    def achar_elemento(self,patt1,patt2):
        try:
            self.navegador=WebDriverWait(self.drive, 10).until(EC.visibility_of_element_located((By.XPATH, patt1)))
            self.navegador.send_keys(patt2)
        except:
            self.chamar_menu()
        
    def chamar_menu(self):
        status=self.chamar_status()
        print("Seu vampiro tem",status[0] ,"moedas de ouro\nPossui",status[1] ,"pedras infernais\nPossui",status[2] ,"fragmentos\nPossui",status[3] ,"/",status[4] ,"de energia\nPossui",status[5] ,"/",status[6] ,"de vida\nSeu nivel é:",status[7] ,"!\nSeu nivel de combate é:",status[8] ,"!!")
        aux=int(input("Escolha a função que deseja fazer:\n1-Caçar humanos.\n2-Caçar demonios.\n3-Caçar no pvp.\n4-Se curar.\n5-Abrir presentes.\n6-Sair.\nEscolha a opção: "))
        match aux:
            case 1:
                aux2=int(input("caçar humanos aonde?\n1-Fazenda.\n2-Aldeia.\n3-Pequena Cidade.\n4-Cidade.\n5-Grande Cidade.\n6-Voltar.\nPressione qualquer outro numero para voltar ao menu principal: "))
                match aux2:
                    case 1:
                        self.cacar_humanos("fazenda")
                    case 2:
                        self.cacar_humanos("aldeia")
                    case 3:
                        self.cacar_humanos("pequena_cidade")
                    case 4:
                        self.cacar_humanos("cidade")
                    case 5:
                        self.cacar_humanos("cidade_grande")
                    case 6:
                        self.chamar_menu()
            case 2:
                aux2=int(input("Caçar demônios em que dificuldade?\n1-Fácil.\n2-Médio.\n3-Difícil.\n4-Voltar.\nColoque o número que deseja:"))
                match aux2:
                    case 1:
                        self.cacar_demonios('facil')
                    case 2:
                        self.cacar_demonios('medio')
                    case 3:
                        self.cacar_demonios('dificil')
                    case 4:
                        self.chamar_menu()
            case 3:
                self.cacar_pvp()
            case 4:
                self.se_curar()
            case 5:
                aux2=int(input("Qual presente deseja abrir?\n1-Presente de ouro.\n2-Presente2 de energia.\n3-Voltar.\nEscolha a opção:"))
                match aux2:
                    case 1:        
                        self.abrir_presente('presente_ouro')
                    case 2:
                        self.abrir_presente('presente_energia')
                    case 3:
                        self.chamar_menu()
            case 6:
                self.drive.quit()
                sys.exit()
                
    def iniciar_navegador(self):
        self.drive.get(self.link_bite_fight)
        self.clicar_elemento(self.xpaths_site['init']['cookie'])
        tempo.sleep(0.5)
        self.clicar_elemento(self.xpaths_site['init']['botao'])
        self.achar_elemento(self.xpaths_site['init']['usuario'],self.login)
        self.achar_elemento(self.xpaths_site['init']['senha'],self.senha)
        tempo.sleep(0.5)
        self.clicar_elemento(self.xpaths_site['init']['entrar'])
        input("pressione qualquer tecla para continuar")
        self.clicar_elemento(self.xpaths_site['init']['botao2'])
        tempo.sleep(7)
        self.drive.close()
        self.drive.switch_to.window(self.drive.window_handles[0])
        self.chamar_menu()
        
    def cacar_humanos(self, local):
        self.clicar_elemento(self.xpaths_site["boton_menu"]["cacar"])
        humanos = self.xpaths_site["human"][local]
        caca_h_n=int(input("Quantas vezes deseja caçar?"))
        print(f"Ira caçar humanos na {local}, {caca_h_n} vezes!")
        self.clicar_elemento(humanos)
        for i in range(caca_h_n):
            site=self.drive.page_source
            soup=BeautifulSoup(site, 'lxml')
            caca_su=soup.find('div', {'class':"buildingDesc"})
            if caca_su is None:
                self.clicar_elemento(self.xpaths_site["buttons"]["return"])
                print(f"\r"+" "*50, end='')
                print(f"\rA caçada numero {i+1} falhou!",end='')
                self.clicar_elemento(humanos)
                self.verificar_pop_up()
            else:
                self.clicar_elemento(self.xpaths_site["buttons"]["repeat"])
                self.verificar_pop_up()
                print(f"\r"+" "*50, end='')
                print(f"\rCaçou {i+1} vezes!",end='')
        self.chamar_menu()
        
    def cacar_demonios(self,dificuldade):
        demonios=self.xpaths_site["demon"][dificuldade]
        self.clicar_elemento(self.xpaths_site["boton_menu"]["city"])
        self.clicar_elemento(self.xpaths_site["boton_menu"]["gruta"])
        caca_d_n=int(input("quantas vezes deseja caçar?"))
        print(f"ira caçar demonios na dificuldade {dificuldade}, {caca_d_n} vezes!")
        for i in range(caca_d_n):
            status=self.chamar_status()
            vida= status[5]
            energ=status[3]
            if vida >= 10000 and energ>=1:
                self.clicar_elemento(demonios)
                self.verificar_pop_up()
                self.clicar_elemento(self.xpaths_site["buttons"]["return"])
                sys.stdout.write("\r")
                sys.stdout.write(f"Energia:{status[3]}/{status[4]}")
                sys.stdout.write(f"  Vida:{status[5]}/{status[6]}")
                sys.stdout.write(f"  Caçou {i+1} vezes!")
                sys.stdout.flush()
            else:
                print("\nVocê esta com a vida baixa, vá descansar!")
                break
        self.chamar_menu()
        
    def chamar_status(self):
        tempo.sleep(1)
        site=self.drive.page_source
        soup=BeautifulSoup(site, 'lxml')
        status_vamp=soup.find('div', {'class':"gold"})
        #text_status=status_vamp.get_text()
        #r'\b\d{1,3}(?:\.\d{3})*(?:\.\d+)\b'
        #'\d+(?:\.\d+)?'
        #\d{1,3}(?:\.\d{3})*(?:\.\d+)?
        #\d{1,3}(?:\.\d{3})*(?:\.\d{1,10})?
        #\d{1,3}(?:\.\d{3})*(?:\.\d{1,10})?|\d+
        #numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
        #numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
        numeros_str = [text.strip() for text in status_vamp.stripped_strings]
        gold,inf_stone,frag,energ,vida,nivel,nivel_com = numeros_str
        energ_v=energ.split('/')
        energia=int(energ_v[0].strip())
        energia_total=int(energ_v[1].strip())
        vida_v=vida.split('/')
        vida_atual=int(vida_v[0].strip().replace(".",""))
        vida_total=int(vida_v[1].strip().replace(".",""))
        gold=int(gold.replace(".",""))
        return [gold, inf_stone, frag, energia, energia_total, vida_atual,vida_total, nivel, nivel_com]
    
    def cacar_pvp(self):
        venceu=0
        perdeu=0
        gold3=0
        gold=0
        self.clicar_elemento(self.xpaths_site["boton_menu"]["cacar"])
        caca_pvp_n=int(input("quantas vezes deseja caçar?"))
        print("ira caçar lobisomens", caca_pvp_n," vezes!")
        for i in range(caca_pvp_n):
            status=self.chamar_status()
            gold1=int(status[0])
            vida= status[5]
            energ=status[3]
            if vida >= 10000 and energ>=1:
                self.clicar_elemento(self.xpaths_site["pvp"]["pvp_escolha"])
                site=self.drive.page_source
                soup=BeautifulSoup(site, 'lxml')
                nome_lobo=soup.find('h2')
                text_lobo=nome_lobo.get_text()
                if "Caça aos lobisomens" in text_lobo:
                    print("\nVocê não foi capaz de encontrar um vítima")
                    break
                print(f"\nIrá atacar o {text_lobo}.")
                self.clicar_elemento(self.xpaths_site["pvp"]["pvp_ataque"])
                self.verificar_pop_up()
                site=self.drive.page_source
                soup=BeautifulSoup(site, 'lxml')
                pvp_re=soup.find('h3')
                pvp_txt=pvp_re.get_text()
                status=self.chamar_status()
                gold2=int(status[0])
                gold3=gold2-gold1
                if 'Zumbie138' in pvp_txt:
                    venceu+=1
                else:
                    perdeu+=1
                print(f"! {pvp_txt} !")
                self.clicar_elemento(self.xpaths_site["buttons"]["return"])
                sys.stdout.write("\r")
                sys.stdout.write(f"Energia:{status[3]}/{status[4]}")
                sys.stdout.write(f"  Vida:{status[5]}/{status[6]}")
                sys.stdout.write(f"  Caçou {i+1} vezes!")
                sys.stdout.flush()
                gold=gold+gold3
            else:
                print("você esta com a vida baixa, vá descansar!")
                break
        print(f"Você venceu {venceu} vezes, e perdeu {perdeu} vezes e saqueou {gold} moedas de ouro.")
        self.chamar_menu()
        
    def se_curar(self):
        aux3=int(input("Deseja se curar aonde?\n1-Igreja.\n2-Poção.\n3-Voltar.\nColoque o número que deseja: "))
        match aux3:
            case 1:
                self.ir_igreja()
            case 2:
                self.beber_pocao()
            case 3:
                self.chamar_menu()
                
    def abrir_presente(self,presente):
        present=self.xpaths_site["curar"][presente]
        visao_geral=self.xpaths_site["boton_menu"]["visao_geral"]
        self.clicar_elemento(visao_geral)
        presente_q=int(input("Quantos presentes deseja abrir?"))
        for i in range(presente_q):
            try:
                self.clicar_elemento(present)
            except:
                break
            print("abriu o",i+1,"presente")
        self.chamar_menu()
        
    def beber_pocao(self):
        visao_geral=self.xpaths_site["boton_menu"]["visao_geral"]
        pocao=self.xpaths_site["curar"]["curar_pocao"]
        self.clicar_elemento(visao_geral)
        try:
            self.clicar_elemento(pocao)
        except:
            print("Não tem poção !!")
        self.chamar_menu()
        
    def ir_igreja(self):
        igreja=self.xpaths_site["boton_menu"]["igreja"]
        city=self.xpaths_site["boton_menu"]["city"]
        curar=self.xpaths_site["curar"]["curar_igreja"]
        self.clicar_elemento(city)
        self.clicar_elemento(igreja)
        self.clicar_elemento(curar)
        self.chamar_menu()
        
    def verificar_pop_up(self):
        site=self.drive.page_source
        soup=BeautifulSoup(site, 'lxml')
        popup_verify=soup.find('div', {'id':"infoPopup"})
        if popup_verify:
            print("missao concluida")
            input("pressione qualquer tecla para continuar")
            # alert=self.drive.switch_to.alert
            # self.clicar_elemento(self.xpaths_site["boton_menu"]["pop_up"])
        
bite_fight= BiteFight()
bite_fight.iniciar_navegador()