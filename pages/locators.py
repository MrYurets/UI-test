from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # Иконка, которая появляется при успешной регистрации

class ProductPageLocators():
    BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket") # Селектор кнопки добавления в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner") # Селектор сообщения о добавлении книги в корзину
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner strong") # Название добавленной книги
    PRICE_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner p strong") # Цена добавленной книги
    NAME_BOOK_PAGE = (By.CSS_SELECTOR, "div h1") # Название кники на странице
    PRICE_BOOK_PAGE = (By.CSS_SELECTOR, ".product_main .price_color") # Цена книги на странице
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default ") # Кнопка добавления в корзину

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p") # Сообщение о том что корзина пуста
    BASKET_PRODUCT = (By.CSS_SELECTOR, "div.basket-title div.row") # Товары, которые есть в корзине

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTERFORM_LINK = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")