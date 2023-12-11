import time
import allure
from store.test_product_page import TestGuestAddToBasketFromProductPage

@allure.title("Сценарий 1.1.1 Авторизованный пользователь добавляет товар в корзину")
@allure.feature('Сайт selenium1py')
def test_scenario_1_1_1(browser):
    """
       1) Пользователь открывает сайт "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       2) Нажимает кнопку добавлять товары в корзину
       3) Тестируем, что гость не видит сообщение о добавлении товара в корзину
       4) Тестируем, что гость не показывается сообщение об успешном добавлении товара пока он не нажимает добавить
       5) Тестируем, что сообщение о добавления в корзину исчезает после нажатия
       6) Тестируем что гость должен увидеть ссылку на регистрацию на странице
       7) Тестирует что гость может нажать на ссылку регистрацию на этой странице
       8) Тестируем что гость переходит в корзину и проверяет что в корзине пусто
       """

    selenium1py = TestGuestAddToBasketFromProductPage(browser)
    selenium1py.open()
    selenium1py.test_guest_can_add_product_to_basket()
    selenium1py.test_guest_cant_see_success_message_after_adding_product_to_basket()
    selenium1py.test_guest_cant_see_success_message()
    selenium1py.test_message_disappeared_after_adding_product_to_basket()
    selenium1py.test_guest_should_see_login_link_on_product_page()
    selenium1py.test_guest_can_go_to_login_page_from_product_page()
    selenium1py.test_guest_cant_see_product_in_basket_opened_from_product_page()
    time.sleep(5)
