from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    EXPECTED_NAME_OF_BOOK = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    ACTUAL_NAME_OF_BOOK = (By.XPATH, "//div[@id='messages']//div[1]//div[1]//strong[1]")
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR,"div[class='col-sm-6 product_main'] p[class='price_color']")
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, "div[class='alertinner '] p strong")
