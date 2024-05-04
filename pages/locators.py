from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    EXPECTED_NAME_OF_BOOK = (By.CSS_SELECTOR, "h1")
    ACTUAL_NAME_OF_BOOK = (By.CSS_SELECTOR, ".alertinner:nth-child(2) strong")
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, ".alertinner p strong")
