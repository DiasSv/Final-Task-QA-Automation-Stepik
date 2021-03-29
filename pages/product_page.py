from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.basket_link)
        basket_link.click()

    def should_be_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.name_product).text == \
               self.browser.find_element(*ProductPageLocators.product_add_succsessful).text, "Product NO add to basket "

    def should_be_right_price(self):
        assert self.browser.find_element(*ProductPageLocators.price).text == \
               self.browser.find_element(*ProductPageLocators.price_add_basket).text, "Price is not okay"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.success_message_after_adding_product_to_basket), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.success_message_after_adding_product_to_basket), \
            "the message was not lost"
