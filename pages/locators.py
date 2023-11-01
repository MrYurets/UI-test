from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTERFORM_LINK = (By.CSS_SELECTOR, "#register_form")