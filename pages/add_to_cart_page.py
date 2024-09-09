from time import sleep

from pages.locators import cart_locators as loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AddToCart(BasePage):
    add_to_cart_url = 'ana-running-short.html'

    def add_product_to_cart(self):
        size = self.find(loc.size_loc)
        size.click()
        color = self.find(loc.color_loc)
        color.click()
        add_cart = self.find(loc.add_to_cart_loc)
        add_cart.click()
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))

    def check_count(self, text):
        count = self.find(loc.count_loc)
        count.click()
        assert count.text == text

    def check_product_in_cart(self, text):
        item_in_cart = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Ana Running Short')]")))
        assert item_in_cart.text == text

    def check_add_to_cart_with_out_selected_size_color(self, text):
        add_cart = self.find(loc.add_to_cart_loc)
        add_cart.click()
        color_error = self.find(loc.color_error_loc)
        assert color_error.text == text
        size_error = self.find(loc.size_error_loc)
        assert size_error.text == text

    def cart(self):
        self.driver.get('https://magento.softwaretestingboard.com/checkout/cart/')
        sleep(4)
