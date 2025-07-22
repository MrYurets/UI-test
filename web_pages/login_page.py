from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def authorization_user(self, login, password):
        """Авторизация пользователя"""
        self.browser.find_element(*LoginPageLocators.LOGIN).send_keys(login)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # Проверяем редирект после авторизации
        WebDriverWait(self.browser, 10).until(
            EC.url_contains('client-113')
        )
        assert "client-113" in self.browser.current_url, f"Expected client page, but got {self.browser.current_url}"

