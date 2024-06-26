from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SEE_IN_BASKET = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    SUCCESS_REG_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASSWORD = (By.NAME, "registration-password1")
    RETRY_REG_PASSWORD = (By.NAME, "registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    EXPECTED_NAME_OF_BOOK = (By.CSS_SELECTOR, "h1")
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")
    ACTUAL_NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")
    MESSAGE_PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p")
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
