from pages.locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_nothing_items_in_basket(self):
        assert not self.is_not_element_present(*BasePageLocators.MESSAGE_EMPTY_BASKET), "The basket is not empty"


    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_EMPTY_BASKET), "The basket is not empty"