from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_add_book_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    browser.execute_script("window.scrollBy(0, 100);")
    name = page.prepare_expected_result("name")
    price = page.prepare_expected_result("price")
    page.click_button_add_to_basket()
    page.add_value_to_popup()
    page.should_be_expected_item_in_basket(name, price)
