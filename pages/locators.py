from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    register_form = (By.ID, "register_form")
    REGISTER_MAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_REGISTER_PASSWORD = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "form#register_form > button.btn-lg")


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
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    SHOULD_BE_EMPTY_BASKET = (By.ID, "basket_formset")
