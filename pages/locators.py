from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    register_form = (By.ID, "register_form")


class ProductPageLocators():
    basket_link = (By.CSS_SELECTOR, "button.btn-add-to-basket")
