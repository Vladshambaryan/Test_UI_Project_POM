from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    sale_url = None
    friendly_page_url = None
    login_page_url = None
    account_create_page_url = None
    ana_running_short_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}/{self.page_url}')

    def open_friendly_page(self):
        self.driver.get(f'{self.base_url}/{self.friendly_page_url}')

    def open_sale_page(self):
        self.driver.get(f'{self.base_url}/{self.sale_url}')

    def open_account_page(self):
        self.driver.get(f'{self.base_url}/{self.account_create_page_url}')

    def open_login_page(self):
        self.driver.get(f'{self.base_url}/{self.login_page_url}')

    def open_ana_running_short_page(self):
        self.driver.get(f'{self.base_url}/{self.ana_running_short_url}')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)
