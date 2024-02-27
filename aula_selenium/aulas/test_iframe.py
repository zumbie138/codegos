from selenium                          import webdriver
from selenium.webdriver.common.by      import By
from selenium.webdriver.support        import expected_conditions as EC
from selenium.webdriver.support.wait   import WebDriverWait
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.maximize_window()
browser.get('https://chercher.tech/practice/frames')
wait = WebDriverWait(browser, 30)

iframe1 = browser.find_element(By.ID, 'frame1')
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys('iframe1')

iframe3 = browser.find_element(By.ID, 'frame3')
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']").click()

browser.switch_to.default_content()
iframe2 = browser.find_element(By.ID, 'frame2')
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value('babycat')
input('')