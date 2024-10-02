import pytest
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://trade.pixtrade.io/pt/login')
    
    #run test
    yield
    
    #teardown
    driver.quit()