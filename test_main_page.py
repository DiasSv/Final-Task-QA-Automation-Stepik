from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # передаем данные
    page.open()  # Открываем страницу
    page.go_to_login_page()  # переходим на стр логин
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()