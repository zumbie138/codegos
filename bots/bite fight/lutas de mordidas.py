import time as tempo
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bp
import requests
from bs4 import BeautifulSoup
import re

#entrando no site
print("Entrando no site do bite fight.")
url ="https://s36-br.bitefight.gameforge.com/user/login"
site = requests.get(url)
drive = webdriver.Firefox()
drive.get(url)
#coockie
tempo.sleep(1)
click_1 = drive.find_element(By.XPATH,'/html/body/div[8]/div/div/span[2]/button[2]')
tempo.sleep(1)
click_1.click()
tempo.sleep(1)
#escrevendo login e senha
print("Escrevendo login e senha")
navegador= drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div[2]/div/div/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td[2]/input')
tempo.sleep(1)
navegador.send_keys("Zumbie138")
tempo.sleep(1)
navegador =drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div[2]/div/div/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[2]/input')
tempo.sleep(1)
navegador.send_keys("Leproso.66")
tempo.sleep(1)
navegador.send_keys(Keys.RETURN)
#clicando para entrar
click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div[2]/div/div/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td[2]/input')
tempo.sleep(0.5/1000)
click_1.click()
tempo.sleep(4)
#começa o loop principal
while True:
    #carrega os status do vampiro
    site=drive.page_source
    soup=BeautifulSoup(site, 'lxml')
    status_vamp=soup.find('div', {'class':"gold"})
    text_status=status_vamp.get_text()
    numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
    numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
    gold,inf_stone,frag,energ,energ_t,vida,vida_t,nivel,nivel_com = numeros_inteiros
    print("Seu vampiro tem",gold ,"moedas de ouro\nPossui",inf_stone ,"pedras infernais\nPossui",frag ,"fragmentos\nPossui",energ ,"/",energ_t ,"de energia\nPossui",vida ,"/",vida_t ,"de vida\nSeu nivel é:",nivel ,"!\nSeu nivel de combate é:",nivel_com ,"!!")
    #fazendo o menu
    print("escolha a função que quer fazer:")
    print("1-caçar humanos\n2-caçar demonios\n3-caçar no pvp\n4-se curar\n5-abrir presentes\n6-sair")
    numero = input("coloque aqui o numero: ")
    if numero == "1":
        #caminho de caçar humanos
        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[6]/a')
        tempo.sleep(1)
        click_1.click()
        while True:
            #sub-menu de caçar humanos
            caca_h=input("caçar humanos aonde?\n1-Fazenda\n2-Aldeia\n3-Pequena Cidade\n4-Cidade\n5-Grande Cidade\nPressione qualquer outro numero para voltar ao menu principal: ")
            if caca_h == "1":
                #caçar humanos na fazenda
                caca_h_n=int(input("Quantas vezes deseja caçar?"))
                print("Ira caçar humanos na fazenda", caca_h_n," vezes!")
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/button')
                tempo.sleep(1)
                click_1.click()
                #loop para caçar humanos na fazenda
                for i in range(caca_h_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    caca_su=soup.find('div', {'class':"buildingDesc"})
                    #verificação se caçada foi bem sucedida
                    if caca_su is None:
                        #caso em que a caçada falhou
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        tempo.sleep(1)
                        print("A caçada numero", i+1,"falhou!")
                        tempo.sleep(1)
                        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/button')
                        tempo.sleep(1)
                        click_1.click()
                        tempo.sleep(1)
                    else:
                        #caso que a caçada deu certo
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span')
                        tempo.sleep(1)
                        click_2.click()
                        print("Caçou", i+1,"vezes!")
                        tempo.sleep(1)
                break
            elif caca_h == "2":
                #caçar humanos na aldeia
                caca_h_n=int(input("Quantas vezes deseja caçar?"))
                print("Ira caçar humanos na aldeia", caca_h_n," vezes!")
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[4]/div/button')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                #loop para caçar humanos na aldeia
                for i in range(caca_h_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    caca_su=soup.find('div', {'class':"buildingDesc"})
                    #teste para verificar se a caçada falhou
                    if caca_su is None:
                        #caçada nao deu certo
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        tempo.sleep(1)
                        print("A caçada numero", i+1,"falhou!")
                        tempo.sleep(1)
                        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[4]/div/button')
                        tempo.sleep(1)
                        click_1.click()
                        tempo.sleep(1)
                    else:
                        #caçada bem sucedida
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span')
                        tempo.sleep(1)
                        click_2.click()
                        print("Caçou", i+1,"vezes!")
                        tempo.sleep(1)
                break
            elif caca_h == "3":
                #caçar humanos na pequena cidade
                caca_h_n=int(input("Quantas vezes deseja caçar?"))
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[6]/div/button')
                click_1.click()
                tempo.sleep(1)
                print("ira caçar humanos na pequena cidade", caca_h_n," vezes!")
                #loop para caçar humanos na pequena cidade
                for i in range(caca_h_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    caca_su=soup.find('div', {'class':"buildingDesc"})
                    #teste para ver se a caçada deu certo
                    if caca_su is None:
                        #caso em que a caçada nao deu certo
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        tempo.sleep(1)
                        print("A caçada numero", i+1,"falhou!")
                        tempo.sleep(1)
                        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[6]/div/button')
                        tempo.sleep(1)
                        click_1.click()
                        tempo.sleep(1)
                    else:
                        #caso em que a caçada deu certo
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span')
                        tempo.sleep(1)
                        click_2.click()
                        print("Caçou", i+1,"vezes!")
                        tempo.sleep(1)
                break
            elif caca_h == "4":
                #caçar humanos na cidade
                caca_h_n=int(input("Quantas vezes deseja caçar?"))
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[8]/div/button')
                click_1.click()
                tempo.sleep(1)
                print("Ira caçar humanos na cidade", caca_h_n," vezes!")
                for i in range(caca_h_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    caca_su=soup.find('div', {'class':"buildingDesc"})
                    if caca_su is None:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        tempo.sleep(1)
                        print("A caçada numero", i+1,"falhou!")
                        tempo.sleep(1)
                        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[8]/div/button')
                        tempo.sleep(1)
                        click_1.click()
                        tempo.sleep(1)
                    else:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span')
                        tempo.sleep(1)
                        click_2.click()
                        print("Caçou", i+1,"vezes!")
                        tempo.sleep(1)
                break
            elif caca_h == "5":
                #caçar humanos na cidade grande
                caca_h_n=int(input("Quantas vezes deseja caçar?"))
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[10]/div/button')
                click_1.click()
                tempo.sleep(1)
                print("Ira caçar humanos na grande cidade", caca_h_n," vezes!")
                for i in range(caca_h_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    caca_su=soup.find('div', {'class':"buildingDesc"})
                    if caca_su is None:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        tempo.sleep(1)
                        print("A caçada numero", i+1,"falhou!")
                        tempo.sleep(1)
                        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div[2]/div/div[10]/div/button')
                        tempo.sleep(1)
                        click_1.click()
                        tempo.sleep(1)
                    else:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div/form/div/div/button/span')
                        tempo.sleep(1)
                        click_2.click()
                        print("Caçou", i+1,"vezes!")
                        tempo.sleep(1)
                break
            else:
                break
            
    elif numero =="2":
        #caminho para caçar demonios
        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[5]/a')
        tempo.sleep(1)
        click_2.click()
        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/a')
        tempo.sleep(1)
        click_2.click()        
        while True:
            #sub-menu dos demonios
            caca_d=input("qual dificuldade você escolhe?\n1-dificil\n2-medio\n3-facil\npressione qualquer numero para voltar ao menu principal: ")
            if caca_d == "1":
                caca_d_n=int(input("quantas vezes deseja caçar?"))
                print("ira caçar demonios na dificuldade dificil", caca_d_n," vezes!")
                for i in range(caca_d_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    status_vamp=soup.find('div', {'class':"gold"})
                    text_status=status_vamp.get_text()
                    numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
                    numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
                    gold,inf_stone,frag,energ,energ_t,vida,vida_t,nivel,nivel_com = numeros_inteiros
                    print("",vida, "/",vida_t,"")
                    if vida >= 10000 and energ>=1:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/form/div/input')
                        tempo.sleep(1)
                        click_2.click()
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        print("caçou", i+1,"vezes")
                        tempo.sleep(1)
                    else:
                        print("você esta com a vida baixa, vá descansar!")
                        i = caca_d_n
                break
            elif caca_d == "2":
                caca_d_n=int(input("quantas vezes deseja caçar?"))
                print("ira caçar demonios na dificuldade medio", caca_d_n," vezes!")
                for i in range(caca_d_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    status_vamp=soup.find('div', {'class':"gold"})
                    text_status=status_vamp.get_text()
                    numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
                    numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
                    gold,inf_stone,frag,energ,energ_t,vida,vida_t,nivel,nivel_com = numeros_inteiros
                    print("",vida, "/",vida_t,"")
                    if vida >= 10000 and energ>=1:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[2]/form/div/input')
                        tempo.sleep(1)
                        click_2.click()
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        print("caçou", i+1,"vezes")
                        tempo.sleep(1)
                    else:
                        print("você esta com a vida baixa, vá descansar!")
                        i = caca_d_n
                break
            elif caca_d == "3":
                caca_d_n=int(input("quantas vezes deseja caçar?"))
                print("ira caçar demonios na dificuldade facil", caca_d_n," vezes!")
                for i in range(caca_d_n):
                    site=drive.page_source
                    soup=BeautifulSoup(site, 'lxml')
                    status_vamp=soup.find('div', {'class':"gold"})
                    text_status=status_vamp.get_text()
                    numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
                    numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
                    gold,inf_stone,frag,energ,energ_t,vida,vida_t,nivel,nivel_com = numeros_inteiros
                    print("",vida, "/",vida_t,"")
                    if vida >= 10000 and energ>=1:
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[1]/form/div/input')
                        tempo.sleep(1)
                        click_2.click()
                        click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                        tempo.sleep(1)
                        click_2.click()
                        print("caçou", i+1,"vezes")
                        tempo.sleep(1)
                    else:
                        print("você esta com a vida ou energia baixa, vá descansar!")
                        i = caca_d_n
                break
            else:
                break
    elif numero =="3":
        #caminho para fazer pvp
        click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[6]/a')
        tempo.sleep(1)
        click_1.click()
        caca_pvp_n=int(input("quantas vezes deseja caçar?"))
        print("ira caçar lobisomens", caca_pvp_n," vezes!")
        for i in range(caca_pvp_n):
            site=drive.page_source
            soup=BeautifulSoup(site, 'lxml')
            status_vamp=soup.find('div', {'class':"gold"})
            text_status=status_vamp.get_text()
            numeros_str = re.findall(r'\d+(?:\.\d+)?', text_status)
            numeros_inteiros=[int(numero_str.replace(".", "")) for numero_str in numeros_str]
            gold,inf_stone,frag,energ,energ_t,vida,vida_t,nivel,nivel_com = numeros_inteiros
            print("",vida, "/",vida_t,"")
            if vida >= 10000 and energ>=1:
                click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[1]/div[2]/div/form[1]/div/div/div/input')
                tempo.sleep(1)
                click_2.click()
                site=drive.page_source
                soup=BeautifulSoup(site, 'lxml')
                nome_lobo=soup.find('h2')
                text_lobo=nome_lobo.get_text()
                print("Irá atacar o",text_lobo,".")
                click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[2]/div/div[2]/table/tbody/tr[9]/td/table/tbody/tr/td[1]/form/div/div/button')
                tempo.sleep(1)
                click_2.click()
                site=drive.page_source
                soup=BeautifulSoup(site, 'lxml')
                pvp_re=soup.find('h3')
                pvp_txt=pvp_re.get_text()
                print(pvp_txt)
                click_2 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/a')
                tempo.sleep(1)
                click_2.click()
                print("caçou", i+1,"vezes")
                tempo.sleep(1)
            else:
                print("você esta com a vida baixa, vá descansar!")
                i = caca_pvp_n
    elif numero == "4":
        while True:
            print("deseja se curar aonde?\n1-na igreja\n2-beber poção")
            cura_d=input("Qual opção deseja: ")
            if cura_d == '1':
                print("indo se curar na igreja")
                #cidade
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[5]/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                #igreja
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[7]/td[2]/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                #curar
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/form/div/div/input')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                break
            elif cura_d =='2':
                print("indo beber poção")
                #visão geral
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[2]/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                #poção
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                break
            else:
                print("numero invalido")
    elif numero == "5":
        while True:
            print("deseja abrir qual presente?\n1-de ouro\n2-de energia")
            presente=input("Qual opção deseja: ")
            if presente == '1':
                #visão geral
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[2]/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                presente_q=int(input("Quantos presentes de energia deseja abrir?: "))
                for i in range(presente_q):
                    click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[2]/div/div/a')
                    tempo.sleep(1)
                    click_1.click()
                    tempo.sleep(2)
                    print("abriu o",i+1,"presente")
                break
            elif presente =='2':
                #visão geral
                click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[2]/a')
                tempo.sleep(1)
                click_1.click()
                tempo.sleep(1)
                presente_q=int(input("Quantos presente de ouro deseja abrir?: "))
                for i in range(presente_q):
                    click_1 = drive.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td[2]/div/div/a')
                    tempo.sleep(1)
                    click_1.click()
                    tempo.sleep(2)
                    print("abriu o",i+1,"presente")
                break
            else:
                print("numero invalido")
    elif numero == "6":
        drive.quit()
        break
    else:
        print("numero invalido")