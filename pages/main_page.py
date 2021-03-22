from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):  # переходит на страницу логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):  # проверяет наличие элемента на странице
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not present"
