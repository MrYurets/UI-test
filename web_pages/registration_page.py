from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    def should_be_registration_page(self):
        """Проверяем, что находимся на странице регистрации"""
        self.should_be_registration_url()
        self.should_be_registration_form()

    def should_be_registration_url(self):
        """Проверяем, что URL страницы содержит 'login'"""
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("login")
        )
        assert "login" in self.browser.current_url, "Can't find 'login' in URL"

    def should_be_registration_form(self):
        """Проверяем, что форма регистрации присутствует на странице"""
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTRATION_FORM)
        )

    def register_user(self, email, password):
        """Заполнение формы регистрации и отправка"""
        self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        # Проверяем, что произошел редирект на страницу после регистрации
        WebDriverWait(self.browser, 10).until(
            EC.url_changes(self.browser.current_url)
        )
        current_url = self.browser.current_url
        assert current_url != self.browser.current_url, f"Registration failed, URL is still {current_url}"