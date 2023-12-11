from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        """Проверяем, что находимся на странице регистрации(когда соблюдаются все проверки)"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяем, что странице есть кнопка Войти"""
        assert self.browser.current_url, "Cant find word login in url"

    def should_be_login_form(self):
        """Проверяем, что есть форма авторизации"""
        assert self.is_element_present(*LoginPageLocators.LOGINFORM_LINK), "Login form link is not presented"

    def should_be_register_form(self):
        """Проверяем, что есть регистрации"""
        assert self.is_element_present(*LoginPageLocators. REGISTERFORM_LINK), "Register form link is not presented"

    def register_new_user(self, email, password):
        """Регистрируем нового пользователя"""
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()