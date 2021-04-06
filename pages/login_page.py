import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL LOGIN IS NOT FOUNDED"  # наличие строки "логин" в url страницы

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not founded"  # наличие формы логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form not founded"
