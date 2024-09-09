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

    def check_count(self):
        count = self.find(loc.count_loc)
        count.click()
        assert count.text == '1'

    def check_product_in_cart(self):
        item_in_cart = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Ana Running Short')]")))
        assert item_in_cart.text == 'Ana Running Short'

    def check_add_to_cart_with_out_selected_size_color(self):
        add_cart = self.find(loc.add_to_cart_loc)
        add_cart.click()
        color_error = self.find(loc.color_error_loc)
        assert color_error.text == 'This is a required field.'
        size_error = self.find(loc.size_error_loc)
        assert size_error.text == 'This is a required field.'


# def select_product(self):
#     short = self.find(ecoloc.short_loc)
#     short.click()
#     size = self.find(ecoloc.size_loc)
#     size.click()
#     color = self.find(ecoloc.color_loc)
#     color.click()
#     add_to_cart = self.find(ecoloc.add_to_cart_loc)
#     add_to_cart.click()
#
# def check_product_in_cart(self, text):
#     short1 = self.find(ecoloc.short1_loc)
#     assert short1.text == text


