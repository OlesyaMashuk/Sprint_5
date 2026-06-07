
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from utils import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestLoginSuccess:
    # тест успешной авторизации

    def test_login_user(self, driver, wait):
        # Нажать"Вход и регистрация"
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
        # Заполненить поля
        email_input = wait.until(EC.visibility_of_element_located(INPUT_EMAIL))
        email_input.send_keys(EXISTING_USER_EMAIL)
        password_input = driver.find_element(*INPUT_PASSWORD)
        password_input.send_keys(EXISTING_USER_PASSWORD)
        # Нажать "Войти"
        wait.until(EC.presence_of_element_located(BTN_SUBMIT_LOGIN)).click()
               
        # Проверка что есть юзер
        user_name = driver.find_element(*USER_NAME_LABEL).text
        assert "User." in user_name
        print("✅ Юзер есть")

        logout_btn = wait.until(EC.element_to_be_clickable(BTN_LOGOUT))
        assert logout_btn.text.strip() == "Выйти"
        print("✅ Пользователь успешно авторизован (кнопка 'Выйти' на месте).")