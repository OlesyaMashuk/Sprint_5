
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from utils import generate_unique_email
from data.test_data import AD_TITLE, AD_DESCRIPTION, AD_PRICE, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from selenium.webdriver.support import expected_conditions

class TestAdCreationAuthorized:
    # создание объявления неавторизованным пользователем

    def test_create_ad_unauthorized(self, driver):
        wait = WebDriverWait(driver, 10)
        # Нажать «Разместить объявление»
        wait.until(EC.element_to_be_clickable(BTN_CREATE_AD)).click()
        # Проверка модального окна
        modal_title = wait.until(EC.visibility_of_element_located(MODAL_AUTH_TITLE))
        
        assert modal_title.is_displayed()
        assert "Чтобы разместить объявление, авторизуйтесь" in modal_title.text


    # создание объявления авторизованным пользователем

    def test_create_ad_authorized(self, driver):
        wait = WebDriverWait(driver, 10)
        # Авторизация
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*INPUT_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*BTN_SUBMIT_LOGIN).click()
        wait.until(EC.visibility_of_element_located(BTN_LOGOUT))
        
        
        # Нажать «Разместить объявление»
        create_ad_btn = wait.until(EC.presence_of_element_located(BTN_CREATE_AD))
        driver.execute_script("arguments[0].click();", create_ad_btn)
        wait.until(EC.visibility_of_element_located(INPUT_TITLE))
       
        # Заполненить поля      
        driver.find_element(*INPUT_TITLE).send_keys(AD_TITLE)
        driver.find_element(*INPUT_DESCRIPTION).send_keys(AD_DESCRIPTION)
        driver.find_element(*INPUT_PRICE).send_keys(AD_PRICE)
        
        
        # Нажать «Опубликовать»
        driver.find_element(*BTN_PUBLISH).click()
        wait.until(expected_conditions.visibility_of_element_located((BTN_LOGOUT)))
        ad_element = wait.until(EC.presence_of_element_located((LOCATOR_NEW_AD)))
        assert ad_element.is_displayed()

   