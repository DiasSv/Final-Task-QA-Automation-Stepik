import pytest

from pages.product_page import ProductPage


# For promo, finding a bug
@pytest.mark.xfail
@pytest.mark.parametrize('links', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                   "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                   "?promo=offer6", "?promo=offer7", "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()  # Нажимаю на кнопку добавления в корзину
    product_page.solve_quiz_and_get_code()  # Провека алерта для получения кода прохождения
    product_page.should_be_product_in_basket()  # Проверяем действительно ли у нас добавился наш товар
    product_page.should_be_right_price()  # Проверяет соотношение цены в корзине и цены товара
