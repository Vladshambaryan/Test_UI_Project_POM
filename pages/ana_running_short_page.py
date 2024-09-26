from time import sleep

from pages.locators import product_locators as prod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from pages.base_page import BasePage


class AnaRunningShort(BasePage):
    ana_running_short_url = 'ana-running-short.html'

    def check_product_name(self):
        product_name = self.find(prod.product_name_loc).text
        assert product_name == "Ana Running Short"

    def check_product_price(self):
        product_price = self.find(prod.product_price_loc).text
        assert product_price == "$40.00"

    def check_product_size(self, text):
        available_sizes = self.find_all(prod.available_sizes_loc)
        sizes = " ".join([size.get_attribute("aria-label") for size in available_sizes])
        assert sizes == text

    def check_product_color(self):
        available_colors = self.find_all(prod.available_colors_loc)
        colors = [color.get_attribute("aria-label") for color in available_colors]
        assert "Black" in colors

    def add_to_compare(self):
        sleep(2)
        compare = self.find(prod.compare_loc)
        compare.click()

    def check_compare_list(self, text):
        sleep(2)
        comparision_list = self.find(prod.comparision_list_loc)
        assert comparision_list.text == text

    def add_product_to_cart(self):
        size = self.find(prod.size_loc)
        size.click()
        color = self.find(prod.color_loc)
        color.click()
        add_cart = self.find(prod.add_to_cart_loc)
        add_cart.click()
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))

    def check_count(self, text):
        count = self.find(prod.count_loc)
        count.click()
        assert count.text == text

    def check_product_in_cart(self, text):
        item_in_cart = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Ana Running Short')]")))
        assert item_in_cart.text == text

    def check_add_to_cart_with_out_selected_size_color(self, text):
        add_cart = self.find(prod.add_to_cart_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", add_cart)  # Прокрутка к элементу

        add_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Add to Cart')]")))
        add_cart.click()
        color_error = self.find(prod.color_error_loc)
        assert color_error.text == text
        size_error = self.find(prod.size_error_loc)
        assert size_error.text == text
