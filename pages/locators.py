from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    register_form = (By.ID, "register_form")


class ProductPageLocators():
    basket_link = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    product_add_succsessful = (By.CSS_SELECTOR, "div.alertinner > strong")
    name_product = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    price = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    price_add_basket = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div.alertinner strong")
    success_message_after_adding_product_to_basket = (By.CSS_SELECTOR, "#messages > div:first-child")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
