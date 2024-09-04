from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    bags_url = None
    jacket_url = None
    shorts_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}/{self.page_url}')

    def open_page_bag(self):
        self.driver.get(f'{self.base_url}/{self.bags_url}')

    def open_page_jacket(self):
        self.driver.get(f'{self.base_url}/{self.jacket_url}')

    def open_page_shorts(self):
        self.driver.get(f'{self.base_url}/{self.shorts_url}')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)
