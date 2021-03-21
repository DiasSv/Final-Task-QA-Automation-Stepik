class BasePage():
    """Мы создаем конструктор, в котором передаются тело
    браузера и ссылка для дальнейшего использования"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
