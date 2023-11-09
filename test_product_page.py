from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestUserAddToBasketFromProductPage():
    """Создаем класс, чтобы тестировать от лица зарегистрированного пользователя """
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org" # Делаем новый email
        password = str(time.time()) + "123" # Делаем новый пароль
        page.register_new_user(email, password) # Регистрируем нового пользователя
        page.should_be_authorized_user() # Проверяем что пользователь авторизован

    def test_user_cant_see_success_message(self, browser):
        """Тестируем, что пользователю не показывается сообщение об успешном добавлении товара пока он его не добавит"""
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Тестируем, что пользователь может добавлять товары в корзину"""
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_form()
        page.add_item_in_basket()
        page.conditions_when_adding_to_cart()

class TestGuestAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """Тестируем, что гость может добавлять товары в корзину"""
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_form()
        page.add_item_in_basket()
        # page.solve_quiz_and_get_code()
        page.conditions_when_adding_to_cart()
        time.sleep(5)


    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """Тестируем, что гость не видит сообщение о добавлении товара в корзину"""
        page = ProductPage(browser, link)
        page.open()
        page.add_item_in_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
         """Тестируем, что гость не показывается сообщение об успешном добавлении товара пока он не нажимает добавить"""
         page = ProductPage(browser, link)
         page.open()
         page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        """Тестируем, что сообщение о добавления в корзину исчезает после нажатия"""
        page = ProductPage(browser, link)
        page.open()
        page.add_item_in_basket()
        page.is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        """Тестируем что гость должен увидеть ссылку на регистрацию на странице"""
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """Тестирует что гость может нажать на ссылку регистрацию на этой странице"""
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """Тестируем что гость переходит в корзину и проверяет что в корзине пусто"""
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_product_basket()
        page.should_be_empty_basket()