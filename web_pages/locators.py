from selenium.webdriver.common.by import By


# Локаторы для страницы авторизации
class LoginPageLocators:
    LOGIN = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Локаторы для страницы клиента
class ClientPageLocators:
    CLIENT_DASHBOARD = (By.CSS_SELECTOR, ".navbar.fixed-top.navbar-expand-lg.navbar-dark.bg-primary.overflow-auto")  # Панель управления
    DEVICES_BUTTON = (By.CSS_SELECTOR, "a.nav-link[href='https://stage-mgt.antisleep.ru/client-113/device']")  # Кнопка "Устройства"
    TOGGLE_COLUMNS_BUTTON = (By.CSS_SELECTOR, '[data-toggle="modal"]') # Кнопка "Переключить столбцы"
    CLOSE_POPUP_BUTTON = (By.XPATH, "(//button[@type='button'][@class='close'][@data-dismiss='modal'])[1]") # Кнопка закрытия поп'апа
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-secondary[name='export'][value='csv']") # Кнопка скачивания отчета
    DOWNLOAD_LINK = (By.XPATH, "//a[contains(text(), 'devices_report')]") # Ссылка скачивания отчета

