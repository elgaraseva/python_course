from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    EXPECTED_NAME_OF_BOOK = (By.CSS_SELECTOR, "h1")
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")
    ACTUAL_NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")
    MESSAGE_PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p")
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
