import time

import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


# For promo, finding a bug
@pytest.mark.need_review
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    # Проверяем, что элемент НЕ находится на странице
    product_page.should_not_be_success_message_after_adding_product_to_basket()


'''Тест предназначен для проверки наличия сообщения об успешном 
добавлении товара в корзину (без добавления товара в корзину'''


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message_after_adding_product_to_basket()


'''Тест проверяет наличие сообщения об успешном добавлении в корзину товара
 (с добавлением товара + используется функция  is_disappeared'''


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking_182/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_item_in_the_basket()  # Пустая ли корзина?
    page.should_be_text_empty_basket()  # Есть ли текст о том, что корзина пустая?


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        email = str(time.time()) + "@fakemailDIASV.org"  # Фейковые данные для регистрации
        password = str(time.time()) + "FakePassword%^$"

        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()  # Нажимаю на кнопку добавления в корзину
        page.should_be_product_in_basket()  # Проверяем действительно ли у нас добавился наш товар
        page.should_be_right_price()  # Проверяет соотношение цены в корзине и цены товара
