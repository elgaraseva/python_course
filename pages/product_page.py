from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def add_value_to_popup(self):
        BasePage.solve_quiz_and_get_code(self)

    def should_be_expected_item_in_basket(self):
        self.should_be_name_of_book()
        self.should_be_price_of_book()

    def should_be_name_of_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        assert name_of_book == "The shellcoder's handbook", f"Wrong book in basket {name_of_book}"
    def should_be_price_of_book(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        assert price_of_book == "9,99 £", "Wrong price"