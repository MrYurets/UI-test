from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Basket form link is not presented"

    def add_item_in_basket(self):
        self.browser.find_element(*BasketPageLocators.BASKET_LINK).click()

    def conditions_when_adding_to_cart(self):
        self.item_price_match()
        self.item_name_match()

    def item_price_match(self):
        price_page = self.browser.find_element(*BasketPageLocators.PRICE_BOOK_PAGE).text
        price_basket = self.browser.find_element(*BasketPageLocators.PRICE_BOOK_BASKET).text
        assert price_page == price_basket, "__product price do not match__"

    def item_name_match(self):
        name_page = self.browser.find_element(*BasketPageLocators.NAME_BOOK_PAGE).text
        name_basket = self.browser.find_element(*BasketPageLocators.NAME_BOOK_BASKET).text
        assert name_page == name_basket, "__product names do not match__"
