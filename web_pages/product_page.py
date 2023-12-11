from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_basket_form(self):
        """Проверяем отображение кнопки добавления в корзину"""
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), "Basket form link is not presented"

    def add_item_in_basket(self):
        """Проверяем работает ли кнопка добавить в корзину"""
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()

    def conditions_when_adding_to_cart(self):
        """Сравниваем название товара и цену товара в корзине, с теми что на странице"""
        self.item_price_match()
        self.item_name_match()

    def item_price_match(self):
        """Проверяем соответсвие цены товара и в корзине"""
        price_page = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_PAGE).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_BASKET).text
        assert price_page == price_basket, "__product price do not match__"

    def item_name_match(self):
        """Проверяем соответсвие названия товара и в корзине"""
        name_page = self.browser.find_element(*ProductPageLocators.NAME_BOOK_PAGE).text
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET).text
        assert name_page == name_basket, "__product names do not match__"

    def should_not_be_success_message(self):
        """Проверяем что нет сообющения о добавлнеии товара в корзину"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self):
        """Проверяем, что сообщение о добавлении товара в корзину исчезло"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"

