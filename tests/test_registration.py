
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from data.test_data import  EXISTING_USER_EMAIL
from utils import generate_unique_email


class TestRegistrationSuccess:
    #Тест успешной регистрации нового пользователя
    def test_register_new_user(self, driver):
        wait = WebDriverWait(driver, 10)
        # Нажать «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
        # Нажать  «Нет аккаунта»
        wait.until(EC.element_to_be_clickable(BTN_NO_ACCOUNT)).click()
        # Генерация данных
        email = generate_unique_email()
        password = "AutoTestPass!"
        
        # Заполнить поля логина и пароля*2
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        driver.find_element(*INPUT_PASSWORD_CONFIRM).send_keys(password)
        
        # Нажать «Создать аккаунт»
        driver.find_element(*BTN_CREATE_ACCOUNT).click()
        
        # Проверка, что кнопка "Вход и регистрация" исчезла
        wait.until(EC.invisibility_of_element_located(BTN_LOGIN_REGISTER))
        assert True
        

        # Проверка, что отображается имя пользователя (User.)
        user_label = wait.until(EC.visibility_of_element_located(USER_NAME_LABEL))
        assert "User." in user_label.text
        
        


class TestRegistrationInvalidEmail:
    #Тест регистрации с некорректным email

    def test_register_invalid_email_format(self, driver):
        wait = WebDriverWait(driver, 10)
        
        # Нажать  «Вход и регистрация»
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
         # Нажать  «Нет аккаунта»
        wait.until(EC.element_to_be_clickable(BTN_NO_ACCOUNT)).click()
        
        # Ввести некорректный email
        invalid_email = "invalid_email_format"
        password = "AutoTestPass!"
        
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(invalid_email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        driver.find_element(*INPUT_PASSWORD_CONFIRM).send_keys(password)
        
        driver.find_element(*BTN_CREATE_ACCOUNT).click()
       
        # Проверка, что есть сообщение об ошибке
        wait.until(EC.visibility_of_element_located(ERROR_MESSAGE_EMAIL))
        error_text = driver.find_element(*ERROR_MESSAGE_EMAIL).text
        
        assert "Ошибка" in error_text
        
        
    

class TestRegistrationExistingUser:
    #Тест регистрации существующего пользователя

    def test_register_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
        # Открыть форму регистрации
        wait.until(EC.element_to_be_clickable(BTN_LOGIN_REGISTER)).click()
        wait.until(EC.element_to_be_clickable(BTN_NO_ACCOUNT)).click()
        
        # Ввести данные существующего поль-ля
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        password = "AutoTestPass!"
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        driver.find_element(*INPUT_PASSWORD_CONFIRM).send_keys(password)
        
        driver.find_element(*BTN_CREATE_ACCOUNT).click()

        
        # Проверка, что есть ошибка
        wait.until(EC.visibility_of_element_located(ERROR_MESSAGE_EMAIL))
        error_text = driver.find_element(*ERROR_MESSAGE_EMAIL).text
        
        assert "Ошибка" in error_text
        