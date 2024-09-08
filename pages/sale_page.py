from pages.locators import sale_locators as loc
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SalePage(BasePage):
    sale_url = 'sale.html'

    def open_page_sale(self):
        self.driver.get(f'{self.base_url}/{self.sale_url}')

    def check_title(self, text):
        page_title = self.find(loc.page_title_loc)
        assert page_title.text == text

    def check_product_count(self):
        products = self.find_all(loc.products_loc)
        product_count = len(products)
        expected_count = product_count
        assert product_count == expected_count

    def check_visible_and_clickable(self):
        products = self.find_all(loc.products_loc)
        for index, product in enumerate(products):
            is_clickable = self.driver.execute_script("return arguments[0].offsetParent !== null;", product)
            assert is_clickable, 'The product is not clickable'

    def women_s_deals_element(self, text):
        prise_on_pands = self.find(loc.pands_loc)
        assert prise_on_pands.text == text

    def mens_bargains_element(self, text):
        mens = self.find(loc.mens_loc)
        assert mens.text == text

