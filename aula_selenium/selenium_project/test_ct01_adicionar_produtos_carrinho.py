import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        #fazer login
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

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

