from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def go_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.basket_link)
        basket_link.click()

    def should_be_product_in_alert(self):
        assert "The shellcoder's handbook" in self.is_element_present(*ProductPageLocators.product_add_succsessful), \
                                                                                         "Product NO add to basket "


