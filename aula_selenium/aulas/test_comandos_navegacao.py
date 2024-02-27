import time
from selenium import webdriver

browser = webdriver.Chrome()


browser.get('https://google.com')
time.sleep(1)
browser.maximize_window()
time.sleep(1)
browser.refresh()
time.sleep(1)
browser.get('https://www.saucedemo.com/')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.switch_to.new_window('tab')
time.sleep(1)
browser.close()
time.sleep(1)
browser.switch_to.new_window('tab')
browser.switch_to.new_window('tab')
browser.quit()
