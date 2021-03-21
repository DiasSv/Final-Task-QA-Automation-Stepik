from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # передаем данные
    page.open()  # Открываем страницу
    page.go_to_login_page()  # переходим на стр логин
    page.should_be_login_link()  # проверяем есть ли ссылка на логин
