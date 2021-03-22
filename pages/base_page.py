from selenium.common.exceptions import NoSuchElementException


class BasePage():
    """Мы создаем конструктор, в котором передаются тело
    браузера и ссылка для дальнейшего использования"""
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    '''Эта функция отвечает за универсальную проверку наличия элемента на странице Возращает булево значение'''
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)
