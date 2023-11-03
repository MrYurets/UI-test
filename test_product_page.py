from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_form()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    page.conditions_when_adding_to_cart()
