from pages.login_page import LoginPage


def test_see_forms(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()