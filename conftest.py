import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5) 
    driver.get("https://qa-desk.education-services.ru/")
    
    yield driver
    
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10) 