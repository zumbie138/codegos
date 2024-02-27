from selenium import webdriver
from selenium.webdriver.common.by import By

#abrir navegador
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#fazer login
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

#confirmar que fez login
assert driver.find_element(By.XPATH, "//span[@class='title']")

#clicar no primeiro item
driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
#adicionar ao carrinho
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
#clicar no carrinho
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()

#clicar continuar comprando
driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()
#clicar no segundo item
driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
#adicionar ao carrinho
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
#clicar no carrinho
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()

#verificar se entrou no carrinho
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
input('')

