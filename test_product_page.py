import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage


# For promo, finding a bug
@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('links', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                   "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                   "?promo=offer6", "?promo=offer7", "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()  # Нажимаю на кнопку добавления в корзину
    product_page.solve_quiz_and_get_code()  # Провека алерта для получения кода прохождения
    product_page.should_be_product_in_basket()  # Проверяем действительно ли у нас добавился наш товар
    product_page.should_be_right_price()  # Проверяет соотношение цены в корзине и цены товара


'''В этом тесте мы проверяем, что после добавление в корзину товара ,
 на странице НЕ появляется сообщение об успешном добавлении товара '''

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    # Проверяем, что элемент НЕ находится на странице
    product_page.should_not_be_success_message_after_adding_product_to_basket()


'''Тест предназначен для проверки наличия сообщения об успешном 
добавлении товара в корзину (без добавления товара в корзину'''

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message_after_adding_product_to_basket()


'''Тест проверяет наличие сообщения об успешном добавлении в корзину товара
 (с добавлением товара + используется функция  is_disappeared'''

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_message_disappeared_after_adding_product_to_basket()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking_182/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_item_in_the_basket()
    page.should_be_text_empty_basket()
