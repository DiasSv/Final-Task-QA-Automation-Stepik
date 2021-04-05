from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    """Функция проверяет есть ли в корзине товары"""

    def should_be_no_item_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SHOULD_BE_EMPTY_BASKET)

    '''Функция проверяет есть ли текст о том, что корзина пуста'''

    def should_be_text_empty_basket(self):
        assert len(self.browser.find_elements(*BasketPageLocators.TEXT_BASKET_IS_EMPTY)) > 0, "Basket no empty"