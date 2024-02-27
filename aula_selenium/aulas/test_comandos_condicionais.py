import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://demo.applitools.com/')
username = browser.find_element(By.ID, 'username')
checkbox_remember_me = browser.find_element(By.XPATH, "//input[@type='checkbox']")

# is_displayed()
print(username.is_displayed())
assert username.is_displayed()

# is_enabled()
print(username.is_enabled())
assert username.is_enabled()

# is_selected()
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

checkbox_remember_me.click()
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()
