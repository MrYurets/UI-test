from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        """Открываем страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Проверяем, что элемент есть на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

