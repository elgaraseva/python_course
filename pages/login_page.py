from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time
import random


class LoginPage(BasePage):
    def click_reg_button(self):
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()

    def register_new_user(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(random.randint(10 ** 9, 10 ** 10 - 1))
        self.should_be_login_form()
        self.should_be_register_form()
        self.write_in_fields(email, password)
        self.click_reg_button()
        self.should_be_success_registration()
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_success_registration(self):
        assert self.is_element_present(
            *BasePageLocators.SUCCESS_REG_MESSAGE), "Message about success registration not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def write_in_fields(self, email="", password=""):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_field.send_keys(password)
        retry_password_field = self.browser.find_element(*LoginPageLocators.RETRY_REG_PASSWORD)
        retry_password_field.send_keys(password)
