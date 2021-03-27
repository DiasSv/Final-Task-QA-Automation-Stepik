from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.basket_link)
        basket_link.click()

    def should_be_product_in_alert(self):
        assert "The shellcoder's handbook" == self.browser.find_element(*ProductPageLocators.product_add_succsessful) \
                                                                                    .text, "Product NO add to basket "

    def should_be_okey_price(self):
        assert self.browser.find_element(*ProductPageLocators.price).text == "£9.99", "the price is not match"
