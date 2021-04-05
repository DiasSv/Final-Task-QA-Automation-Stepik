import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # передаем данные
    page.open()  # Открываем страницу
    page.go_to_login_page()  # переходим на стр логин
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()  # Переходим на страницу корзины
    page.should_be_no_item_in_the_basket()  # Проверяем нет ли в корзине товаров
    page.should_be_text_empty_basket()  # Проверяем, есть ли текст о том , что корзина пуста


'''Пример группировки тестов в один класс и его маркировки, для дальнейшего использования'''


@pytest.mark.login_guest
class TestLoginMainPage():
    def test_guest_can_go_to_login_page(self):
        pass

    def test_guest_should_see_login_link(self):
        pass
