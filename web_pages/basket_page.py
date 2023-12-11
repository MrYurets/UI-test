from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_basket(self):
        """Проверяем что нет сообщения о товарах в корзине"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            "There are products in the basket, but should not be"
    def should_be_empty_basket(self):
        """Проверяем что есть сообщение о том, что корзина пустая"""
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "There is no message 'Your basket is empty.'"
