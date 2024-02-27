import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.saucedemo.com/')

# find_element()
# username = browser.find_element(By.ID, 'user-name')
# password = browser.find_element(By.ID, 'password')

# send_keys
# username.send_keys('standard_user')
# password.send_keys('secret_sauce')

# find_elements()
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
print(auth_fields)
print(len(auth_fields))
assert len(auth_fields) == 1, 'O número de elementos encontrados é diferente do esperado'

time.sleep(2)
browser.quit()
