from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):
    """Тестируем, что гость может добавлять товары в корзмину"""
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_form()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    page.conditions_when_adding_to_cart()
    time.sleep(5)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Тестируем,что гость не видит сообщение о добавлении товарав корзину"""
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
     """Тестируем, что гость не показывается сообщение об успешном добавлении товара пока он не нажимает добавить"""
     page = ProductPage(browser, link)
     page.open()
     page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Тестируем,что сообщение о добавления в корзину исчезает после нажатия"""
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    """Тестируем что гость должен увидеть ссылку на рагистрациию настранице"""
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тестирует что гость может нажать на ссылку регистрациир на этой странице"""
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Тестируем что гость переходит в корзину и проверяет что в корзине пусто"""
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_basket()
    page.should_be_empty_basket()