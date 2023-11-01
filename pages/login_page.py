from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Cant find word login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGINFORM_LINK), "Login form link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators. REGISTERFORM_LINK), "Register form link is not presented"