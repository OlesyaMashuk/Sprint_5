
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from utils import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestLogout:
    # Тест разлогина пользователя

    def test_logout_user(self, driver, wait):
        # Авторизация польз-ля
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*INPUT_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*BTN_SUBMIT_LOGIN).click()
        
        wait.until(EC.element_to_be_clickable(BTN_LOGOUT))
        
        # Нажать  «Выйти»
        wait.until(EC.element_to_be_clickable(BTN_LOGOUT)).click()
        
        # Проверки, что есть кнопка "Вход и регистрация"
        login_btn = driver.find_element(*BTN_LOGIN_REGISTER)
        assert login_btn.is_displayed()
        
        # екста "User." больше нет
        user_elements = driver.find_elements(*USER_NAME_LABEL)
        assert len(user_elements) == 0