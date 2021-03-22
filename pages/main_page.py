from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):  # переходит на страницу логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        '''
        Теперь в тесте нам не нужно думать про
        инициализацию страницы: она уже создана. Сохранив возвращаемое значение в переменную, мы можем использовать
        методы новой страницы в тесте 
        
        минусы: 
        если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;
        большая связность кода — при изменении логики придется менять возвращаемое значение;
        сложнее понимать код, так как страница инициализируется неявно;
        образуются циклические зависимости, что часто приводит к ошибкам.
        '''

        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):  # проверяет наличие элемента на странице
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not present"
