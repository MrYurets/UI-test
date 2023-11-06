from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTERFORM_LINK = (By.CSS_SELECTOR, "#register_form")

class BasketPageLocators():
    BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket") # Селектор кнопки добавления  в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner") # Селектор сообщения о добавлении книги в корзину
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner strong") # Название добавленной книги
    PRICE_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner p strong") # Цена добавленной книги
    NAME_BOOK_PAGE = (By.CSS_SELECTOR, "div h1") # Название кники на странице
    PRICE_BOOK_PAGE = (By.CSS_SELECTOR, ".product_main .price_color") # Цена книги на странице

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")