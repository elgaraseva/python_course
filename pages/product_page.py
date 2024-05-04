from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def add_value_to_popup(self):
        BasePage.solve_quiz_and_get_code(self)

    def prepare_expected_result(self, field_name=""):
        if field_name == "name": expected_result = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME_OF_BOOK).text
        if field_name == "price": expected_result = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE_OF_BOOK).text
        return expected_result

    def should_be_expected_item_in_basket(self, actual_name="", actual_price=""):
        self.should_be_name_of_book(expected_name=actual_name)
        self.should_be_price_of_book(expected_price=actual_price)

    def should_be_name_of_book(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.ACTUAL_NAME_OF_BOOK).text
        assert actual_name == expected_name, f"The book {actual_name} in basket doesn't equal {expected_name}"

    def should_be_price_of_book(self, expected_price):
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_OF_BOOK).text
        assert actual_price == expected_price, f"The price {actual_price} in basket doesn't equal {expected_price}"
