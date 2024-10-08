from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import eco_friendly_locator as ecoloc
from pages.base_page import BasePage

class EcoFriendly(BasePage):

    friendly_page_url = 'collections/eco-friendly.html'

    def sort_by_price_and_check_correct_sort(self):
        sort_select = self.find(ecoloc.sort_select_loc)
        select = Select(sort_select)
        select.select_by_value('price')
        prices = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='price']"))
        )
        price_values = []
        for price in prices:
            price.text.replace('$', '').replace(',', '')
        assert price_values == sorted(price_values)

    def enter_search_text(self, text):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)

    def check_search_functionality(self, test):
        search_results = self.find(ecoloc.search_results_loc)
        assert search_results.text == test

    def filter_products_by_price(self):
        price_filter = self.find(ecoloc.price_filter_loc)
        price_filter.click()
        sleep(2)
        price_range = self.find(ecoloc.price_range_loc)
        price_range.click()

    def check_filter_products_by_price(self, text):
        sleep(2)
        filtered = self.find(ecoloc.filtered_loc)
        print(filtered.text)
        assert filtered.text == text

    def verification_product_prices(self, text):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, "span.price")
        product_prices = [price.text.replace("$", "") for price in price_elements if price.text.strip()]
        assert product_prices == text

    def verification_product_size(self, text):
        product_elements = self.find_all(ecoloc.product_elements_loc)
        product_sizes = [element.text for element in product_elements if element.text.strip()]
        assert product_sizes == text

    def verification_product_names(self, text):
        sleep(3)
        product_element = self.find_all(ecoloc.product_element_loc)
        sleep(3)
        product_names = [element.text for element in product_element]
        assert product_names == text


