from pages.locators import sale_locators as loc
from pages.base_page import BasePage


class SalePage(BasePage):

    sale_url = 'sale.html'

    def check_title(self, text):
        page_title = self.find(loc.page_title_loc)
        assert page_title.text == text

    def check_product_count(self):
        products = self.find_all(loc.products_loc)
        product_count = len(products)
        expected_count = product_count
        assert product_count == expected_count

    def women_s_deals_element(self, text):
        prise_on_pands = self.find(loc.pands_loc)
        assert prise_on_pands.text == text

    def mens_bargains_element(self, text):
        mens = self.find(loc.mens_loc)
        assert mens.text == text

