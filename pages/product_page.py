from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def go_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.basket_link)
        basket_link.click()

