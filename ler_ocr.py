from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image
import io

# Configurando o driver do Selenium (neste exemplo, Chrome)
driver = webdriver.Chrome()

# Acessando a página com o captcha
url = "http://esaj.tjba.jus.br/cpopg/open.do"
driver.get(url)

# Localizando o elemento da imagem do captcha
captcha_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='defaultCaptchaImage']")))
captcha_location = captcha_element.location
captcha_size = captcha_element.size

screenshot = driver.get_screenshot_as_png()
captcha_image = Image.open(io.BytesIO(screenshot))
captcha_image = captcha_image.crop((
    captcha_location['x'], captcha_location['y'],
    captcha_location['x'] +
    captcha_size['width'], captcha_location['y'] + captcha_size['height']
))

captcha_image.save("captcha.png")
# Utilizando o pytesseract para realizar OCR na imagem do captcha
captcha_text = pytesseract.image_to_string(captcha_image)



print("Texto do Captcha:", captcha_text)

input("Pressione qualquer tecla para sair...")
driver.quit()