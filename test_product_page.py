import time

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_add_book_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    browser.execute_script("window.scrollBy(0, 100);")
    page.click_button_add_to_basket()  # выполняем метод страницы - нажимаем на кнопку добавления в корзину
    page.add_value_to_popup()
    page.should_be_expected_item_in_basket()

