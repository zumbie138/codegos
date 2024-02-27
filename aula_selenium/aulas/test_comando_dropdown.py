from selenium                          import webdriver
from selenium.webdriver.common.by      import By
from selenium.webdriver.support        import expected_conditions as EC
from selenium.webdriver.support.wait   import WebDriverWait
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.maximize_window()
browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')
wait = WebDriverWait(browser, 30)

dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
dropdown_products.select_by_visible_text('Google')
input('')