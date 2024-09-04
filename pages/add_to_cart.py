from selenium.webdriver.common.by import By
from pages.locators import sale_locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCart(BasePage):
    page_url = 'collections/eco-friendly.html'

    def add_to_cart_button(self):
        short = self.find(loc.short_loc)
        short.click()
        add_cart = self.find(loc.add_cart_loc)
        add_cart.click()

    def check_error(self):
        select_color = self.find(loc.select_color_loc)
        assert select_color.text == 'This is a required field.'
        select_size = self.find(loc.select_size_loc)
        assert select_size.text == 'This is a required field.'

    def add_product_in_cart(self):
        short = self.find(loc.short_loc)
        short.click()
        size = self.find(loc.size_loc)
        size.click()
        color = self.find(loc.color_loc)
        color.click()
        add_cart = self.find(loc.add_cart_loc)
        add_cart.click()

    def check_product_in_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))
        self.find(loc.count_loc)
        count = self.find(loc.count_loc)
        count.click()
        item_in_cart = self.find(loc.item_in_cart_loc)
        print(f'{item_in_cart.text} присутствует в корзине')
        assert item_in_cart.text == 'Ana Running Short'
